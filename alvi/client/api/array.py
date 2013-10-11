#TODO consider using unified name instead of item, element and node
#take into account possible problems with number/names of parameters

CONTAINER = "Array"

def create_element(pipe, id, value):
    pipe.send('create_element', (id, ), dict(
        id=id,
        value=value,
    ))


def update_element(pipe, id, value):
    pipe.send('update_element', (id, ), dict(
        id=id,
        value=value,
    ))
