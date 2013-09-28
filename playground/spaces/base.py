class Space:
    def update_stats(self, name, value):
        return ('update_stats', dict(
            name=name,
            value=value,
        ))