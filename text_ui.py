#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import json
import logging

from app_inst import AppInst
from app_manager import AppManager

_APPS_INFO_EXAMPLE = """
========================== Apps Info Example ==========================
[
    {
        "name": "app1",
        "cmd": "cmd1",
        "tags": "tag0,tag1"
    },
    {
        "name": "app2",
        "cmd": "cmd2",
        "tags": "tag0,tag2"
    }
]
=======================================================================
"""


class TextUI(object):
    def __init__(self, apps_info):
        self.app_manager = AppManager()

        logging.debug("apps info: %s", apps_info)
        for app_info in apps_info:
            app = AppInst(app_info["name"], app_info["cmd"], app_info["tags"])
            self.app_manager.add_app(app)

    def _pretty_list_apps(self, apps):
        print("================================ Apps ================================")
        index = 0
        for app in apps:
            index += 1
            print("%-15s" % app.name, end="")
            if index % 5 == 0:
                print()
        if index % 5 != 0:
            print()
        print("======================================================================")

    def _pretty_list_tags(self, tags):
        print("================================ Tags ================================")
        index = 0
        for tag in tags:
            index += 1
            print("%-15s" % tag, end="")
            if index % 5 == 0:
                print()
        if index % 5 != 0:
            print()
        print("======================================================================")

    def cmd_list_apps(self):
        apps = self.app_manager.list_all_apps()
        self._pretty_list_apps(apps)

    def cmd_list_tags(self):
        tags = self.app_manager.list_all_tags()
        self._pretty_list_tags(tags)

    def cmd_select_apps(self, cmd):
        if len(cmd) != 2:
            print("Cmd error, check your input, try again!")
            return

        tags_str = cmd[1]
        tags = set(tags_str.split(","))
        apps = self.app_manager.select_app_by_tags(tags)
        self._pretty_list_apps(apps)

    def cmd_run_app(self, cmd):
        if len(cmd) != 2:
            print("Cmd error, check your input, try again!")
            return

        name = cmd[1]
        app = self.app_manager.get_app_by_name(name)
        if app is not None:
            ret, info = app.run()
            if ret:
                print("Run success, wait for a moment!")
            else:
                print("Run fail,", info)
        else:
            print("Can not find %s, add it to apps.info first!" % name)

    def cmd_quit(self):
        sys.exit(0)

    def cmd_help(self):
        print("Cmd: list(l)                - show all apps")
        print("Cmd: tags(t)                - show all tags")
        print("Cmd: select(s) tag1,tag2    - select app by tags")
        print("Cmd: run(r) app             - start app")
        print("Cmd: quit(q)                - quit")
        print("Cmd: help(h)                - show this help")

    def run(self):
        self.cmd_help()

        while True:
            cmd_str = input("Please Input Your Cmd: ")
            logging.info(cmd_str)

            cmd_str = cmd_str.strip()
            if len(cmd_str) == 0:
                continue

            cmd = cmd_str.split(" ", 1)
            if cmd[0] == "list" or cmd[0] == "l":
                self.cmd_list_apps()
            elif cmd[0] == "tags" or cmd[0] == "t":
                self.cmd_list_tags()
            elif cmd[0] == "select" or cmd[0] == "s":
                self.cmd_select_apps(cmd)
            elif cmd[0] == "run" or cmd[0] == "r":
                self.cmd_run_app(cmd)
            elif cmd[0] == "quit" or cmd[0] == "q":
                self.cmd_quit()
            elif cmd[0] == "help" or cmd[0] == "h":
                self.cmd_help()
            else:
                print("Unknown cmd, try again!")


def main(f_apps):
    if not os.path.exists(f_apps):
        print("Please input your app info in the file: %s" % f_apps)
        print(_APPS_INFO_EXAMPLE)

        input("Press Enter key to continue ...")
        sys.exit(0)

    with open(f_apps, encoding="utf-8") as fh:
        apps_info = json.load(fh)
        ui = TextUI(apps_info)
        ui.run()


if __name__ == '__main__':
    logging.basicConfig(level=logging.WARNING,
                        format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")

    main("./apps.info")
