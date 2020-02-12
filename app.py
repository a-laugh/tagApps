import subprocess


class App(object):
    def __init__(self, name, cmd, tags):
        self.name = name
        self.cmd = cmd
        self.tags = set(tags.split(','))

    def run(self):
        subprocess.Popen(self.cmd)


if __name__ == '__main__':
    app = App("VSCode", "C:\\Program Files\\Microsoft VS Code\\Code.exe", "tool,program,editor")
    app.run()
