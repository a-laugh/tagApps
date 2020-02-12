import subprocess

from app_repo import AppRepo


class App(object):
    def __init__(self, name, icon, cmd, tags):
        self._app_inst_repo = AppRepo()
        self.name = name
        self.icon = icon
        self.cmd = cmd
        self.tags = set(tags.split('|'))

    def update(self, icon, cmd, tags):
        self.icon = icon
        self.cmd = cmd
        self.tags = set(tags.split('|'))

    def run(self):
        subprocess.Popen(self.cmd)

    def save(self):
        self._app_inst_repo.save(self)

    def delete(self):
        self._app_inst_repo.delete(self)


if __name__ == '__main__':
    app = App("VSCode", "", "C:\\Program Files\\Microsoft VS Code\\Code.exe", "工作|编程")
    app.save()
    from app_repo import g_app_dict
    for name, app in g_app_dict.items():
        print(name, app.cmd, app.tags)
