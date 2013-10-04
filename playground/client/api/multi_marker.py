def create(pipe, id, name):
    pipe.send('create_multi_marker', (id,), dict(
        id=id,
        name=name,
    ))


def add(pipe, id, item_id):
    pipe.send('multi_marker_add_item', (id,), dict(
        id=id,
        item_id=item_id,
    ))
