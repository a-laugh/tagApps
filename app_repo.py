g_app_dict = {}


class AppRepo(object):
    def __init__(self):
        super(AppRepo, self).__init__()

    def save(self, app):
        g_app_dict[app.name] = app

    def delete(self, app):
        del g_app_dict[app.name]
