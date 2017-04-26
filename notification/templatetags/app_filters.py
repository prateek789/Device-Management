from django import template
import timeago,datetime

register = template.Library()

@register.filter(name='get_due_date_string')
def get_due_date_string(value):
    format_date = timeago.format(value.strftime("%Y-%m-%d %H:%M:%S"),datetime.datetime.now())
    return format_date
