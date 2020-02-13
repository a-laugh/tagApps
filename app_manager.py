from app_inst import AppInst


class AppManager(object):
    def __init__(self):
        self.apps = {}

    def add_app(self, app: AppInst):
        self.apps[app.name] = app

    def list_all_apps(self):
        apps = []
        for app in self.apps.values():
            apps.append(app)

        return apps

    def list_all_tags(self):
        tags = set()
        for app in self.apps.values():
            tags.update(app.tags)

        return sorted(list(tags))

    def select_app_by_tags(self, tags: set):
        apps = []
        for app in self.apps.values():
            if tags.issubset(app.tags):
                apps.append(app)

        return apps

    def get_app_by_name(self, name):
        if name in self.apps:
            return self.apps[name]
        else:
            return None
