from django.forms import ModelForm, HiddenInput, inlineformset_factory, modelformset_factory
from nested_formset import nestedformset_factory

from .models import Books, Author, Publisher

class AuthorForm(ModelForm):

    class Meta:
        model = Author
        fields = "__all__"


class PublisherForm(ModelForm):

    class Meta:
        model = Publisher
        fields = "__all__"



class BookForm(ModelForm):

    class Meta:
        model = Books
        fields = "__all__"


