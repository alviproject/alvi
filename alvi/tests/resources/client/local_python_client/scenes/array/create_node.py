from alvi.client.containers import Array
from alvi.client.scenes.base import Scene
from django import forms


class ArrayCreateNode(Scene):
    class Form(Scene.Form):
        n = forms.IntegerField(initial=4)

    def run(self, array, options):
        n = int(options['n'])
        array.init(n)
        for i in range(n):
            array[i] = i
        array.sync()

    @classmethod
    def container_class(cls):
        return Array