# coding: utf-8

from nose.tools import eq_

from app_inst import AppInst


class TestAppInst(object):
    def __init__(self):
        self.app = AppInst("app_name", "app_cmd", "tag_a,tag_b")

    def test_init(self):
        eq_(self.app.name, "app_name")
        eq_(self.app.cmd, "app_cmd")
        eq_(self.app.tags, {"tag_a", "tag_b"})
