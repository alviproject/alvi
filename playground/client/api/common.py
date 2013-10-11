def create_marker(pipe, id, name, item_id):
    pipe.send('create_marker', (id,), dict(
        id=id,
        name=name,
        item_id=item_id,
    ))


def move_marker(pipe, id, item_id):
    pipe.send('move_marker', (id,), dict(
        id=id,
        item_id=item_id,
    ))


def remove_marker(pipe, id):
    pipe.send('remove_marker', (id,), dict(
        id=id,
    ))


def update_stats(pipe, name, value):
    pipe.send("update_stats", (name, ), dict(
        name=name,
        value=value
    ))


def create_multi_marker(pipe, id, name):
    pipe.send('create_multi_marker', (id,), dict(
        id=id,
        name=name,
    ))


def multi_marker_add_item(pipe, id, item_id):
    pipe.send('multi_marker_add_item', (id, item_id), dict(
        id=id,
        item_id=item_id,
    ))