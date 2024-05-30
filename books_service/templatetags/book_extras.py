from ..models import Books, Author, Publisher
from django import template

register = template.Library()


@register.simple_tag
def get_authors():
    authors = Author.objects.all()
    return authors


@register.simple_tag
def get_pub():
    publishers = Publisher.objects.all()
    return publishers
