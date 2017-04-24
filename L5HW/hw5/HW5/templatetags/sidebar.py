from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.inclusion_tag('bootstrap_button.html')
def bootstrap_button(text, style="default"):
    return {
        'style': style.lower(),
        'text': text
    }
