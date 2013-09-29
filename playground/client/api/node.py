def create(pipe, id, parent_id, value):
    pipe.send('create_node', (id, ), dict(
        id=id,
        parent_id=parent_id,
        value=value,
    ))


def update(pipe, id, value):
    pipe.send('update_node', (id, ), dict(
        id=id,
        value=value,
    ))