import subprocess


class AppInst(object):
    def __init__(self, name, cmd, tags):
        self.name = name
        self.cmd = cmd
        self.tags = set(tags.split(','))

    def run(self):
        subprocess.Popen(self.cmd)
