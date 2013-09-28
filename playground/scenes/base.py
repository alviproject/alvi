import abc
import inspect
import collections
import playground.utils.enum as enum

import django.forms.fields
import django.forms


class Scene(metaclass=abc.ABCMeta):
    Container = None  # override in inherited class

    def __init__(self):
        container_class = self.container_implementation()
        container = container_class(pipe)
        #self._container =

    @enum.unique
    class SyncPoints(enum.Enum):
        basic = 1

    class Form(django.forms.Form):
        n = django.forms.fields.IntegerField(min_value=1, max_value=2048, initial=1024, label="Number of elements")

    def name(self):
        name = self.__class__.__name__
        ##change from camel case to space delimeted
        #name = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', name)
        #name = name.replace("_", " ")
        return name

    def container_implementation(self):
        #TODO
        return self.container_class().implementations()[0]

    def template(self):
        return self.container_implementation().space_class().template


