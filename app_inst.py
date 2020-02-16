# coding: utf-8

import subprocess


class AppInst(object):
    def __init__(self, name, cmd, tags):
        self.name = name
        self.cmd = cmd
        self.tags = set(tags.split(','))

    def run(self):
        try:
            subprocess.Popen(self.cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return True, ""
        except Exception as e:
            return False, e
