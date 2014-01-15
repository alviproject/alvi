from alvi.client.data_generators.base import DataGenerator
from django import forms


class SequencedDataGenerator(DataGenerator):
    class Form(DataGenerator.Form):
        descending = forms.BooleanField(label="Descending", initial=True, required=False)

    def _values(self):
        return ((self.quantity()-i-1 if self.descending else i) for i in range(self.quantity())).__iter__()

    @property
    def descending(self):
        return self._options['descending']