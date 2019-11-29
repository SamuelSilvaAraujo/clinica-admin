from datetime import datetime

from django import template

register = template.Library()


@register.filter()
def age(date):
    today = datetime.now()
    return (today.year - date.year) - ((today.month, today.day) < (date.month, date.day))