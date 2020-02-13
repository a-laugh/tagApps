from nose.tools import eq_

from app_inst import AppInst
from app_manager import AppManager


class TestAppManager(object):
    def __init__(self):
        self.app_manager = AppManager()
        self.app1 = AppInst("app1", "cmd1", "tag,tag1a,tag1b")
        self.app_manager.add_app(self.app1)
        self.app2 = AppInst("app2", "cmd2", "tag,tag2a,tag2b")
        self.app_manager.add_app(self.app2)

    def test_list_all_apps(self):
        apps = self.app_manager.list_all_apps()
        eq_(len(apps), 2)
        expect = {self.app1, self.app2}
        eq_(expect, set(apps))

    def test_list_all_tags(self):
        tags = self.app_manager.list_all_tags()
        expect = ["tag", "tag1a", "tag1b", "tag2a", "tag2b"]
        eq_(expect, tags)

    def test_select_app_by_tags(self):
        apps = self.app_manager.select_app_by_tags({"tag2a"})
        eq_(len(apps), 1)
        eq_(self.app2, apps[0])

    def test_get_app_by_name(self):
        app = self.app_manager.get_app_by_name("app1")
        eq_(self.app1, app)
