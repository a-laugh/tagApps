# coding: utf-8

import subprocess


class AppInst(object):
    def __init__(self, name, cmd, tags):
        self.name = name
        self.cmd = cmd
        self.tags = set(tags.split(','))

    def run(self):
        subprocess.Popen(self.cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
