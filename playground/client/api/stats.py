def update(pipe, name, value):
    pipe.send("update_stats", (name, ), dict(
        name=name,
        value=value
    ))