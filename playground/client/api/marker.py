def create(pipe, id, name, item_id):
    pipe.send('create_marker', (id,), dict(
        id=id,
        name=name,
        item_id=item_id,
    ))


def move(pipe, id, item_id):
    pipe.send('move_marker', (id,), dict(
        id=id,
        item_id=item_id,
    ))


def remove(pipe, id):
    pipe.send('remove_marker', (id,), dict(
        id=id,
    ))