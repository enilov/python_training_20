# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_delete_some_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name = "test"))
    old_groups = db.get_group_list()
    index = random.randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index+1] = []
    assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

