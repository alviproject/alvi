import functools


def action(method_or_return_action_name):
    """
    decorator marking Container method as an action
    all marked method will be processed by ContainerMeta
    """

    if callable(method_or_return_action_name):
        #first decorator argument is a method, that means that @action was called without parameters
        #just set return_action_name attribute and return original method
        method = method_or_return_action_name
        method._return_action_name = method.__name__
        return method

    #first decorator argument is not a method, which implies that means that decorator was called like that:
    # @action('return_action_name')
    return_action_name = method_or_return_action_name

    def _action(container_method):
        @functools.wraps(container_method)
        def wrapper(*args, **kwargs):
            return container_method(*args, **kwargs)
        wrapper._return_action_name = return_action_name
        return wrapper
    return _action


class ContainerMeta(type):
    """metaclass that saves all action methods in class level dictionary"""
    def __init__(cls, name, bases, attributes):
        cls.actions = {}
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            try:
                return_action_name = attr._return_action_name
                cls.actions[attr_name] = (return_action_name, attr)
            except AttributeError:
                pass
        super().__init__(name, bases, attributes)


class Container(metaclass=ContainerMeta):
    def evaluate_action(self, action_name, **kwargs):
        try:
            return_action_name, action_method = self.__class__.actions[action_name]
        except KeyError as x:
            raise RuntimeError("Class %s does not implement method %s that was called by client."
                               % (self.__class__.__name__, action_name), x)
        args = action_method(self, **kwargs)
        return return_action_name, args

    @classmethod
    def implementations(cls):
        return cls.__subclasses__()

    @action
    def update_stats(self, **kwargs):
        return kwargs

    @action
    def finish(self, **kwargs):
        return kwargs

    @action
    def create_marker(self, **kwargs):
        return kwargs

    @action
    def move_marker(self, **kwargs):
        return kwargs

    @action
    def remove_marker(self, **kwargs):
        return kwargs

    @action
    def create_multi_marker(self, **kwargs):
        return kwargs

    @action
    def multi_marker_append(self, **kwargs):
        return kwargs

    @action
    def multi_marker_remove(self, **kwargs):
        return kwargs