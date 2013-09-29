def create(pipe, id, value):
    pipe.send('create_element', (id, ), dict(
        id=id,
        value=value,
    ))


def update(pipe, id, value):
    pipe.send('update_element', (id, ), dict(
        id=id,
        value=value,
    ))
