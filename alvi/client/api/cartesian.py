CONTAINER = "Cartesian"


def create_point(pipe, id, x, y):
    pipe.send(
        'create_point',
        (id, ),
        dict(
            id=id,
            x=x,
            y=y,
        ))


def create_line(pipe, id, id_point_from, id_point_to):
    pipe.send(
        'create_line',
        (id, ),
        dict(
            id=id,
            id_point_from=id_point_from,
            id_point_to=id_point_to
        ))


def update_line(pipe, id, id_point_from, id_point_to):
    pipe.send(
        'update_line',
        (id, ),
        dict(
            id=id,
            id_point_from=id_point_from,
            id_point_to=id_point_to
        ))