import abc
from django import forms


class DataGenerator(metaclass=abc.ABCMeta):
    class Form(forms.Form):
        n = forms.IntegerField(min_value=1, max_value=256, label='Elements', initial=64)

    def __init__(self, options):
        form = self.Form(options)
        if not form.is_valid():
            raise forms.ValidationError(form.errors)
        self._options = form.cleaned_data
        self._values_iterator = None

    @property
    def values(self):
        """
        return iterator over self.quantity of subsequent generated values
        """
        if not self._values_iterator:
            self._values_iterator = self._values()
        return self._values_iterator

    @abc.abstractmethod
    def _values(self):
        """abstract method that shall return iterator to  subsequent generated values"""
        raise NotImplementedError

    def quantity(self):
        return self._options['n']