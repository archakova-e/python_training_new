from model.group import Group


def test_1_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="test")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_2_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group())
    app.group.modify_first_group(Group(name="new_name"))


def test_3_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group())


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    app.group.modify_first_group(Group(header="new_header"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="test"))
    app.group.modify_first_group(Group(footer="new_footer"))
