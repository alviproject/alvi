import abc

import django.forms.fields
import django.forms


class Scene(metaclass=abc.ABCMeta):
    Container = None  # override in inherited class

    def name(self):
        name = self.__class__.__name__
        ##change from camel case to space delimeted
        #name = re.sub(r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))', r' \1', name)
        #name = name.replace("_", " ")
        return name

    @classmethod
    def container_implementation(cls):
        #TODO
        return cls.container_class().implementations()[0]

    @classmethod
    def template(cls):
        #TODO
        return cls.container_implementation().template


