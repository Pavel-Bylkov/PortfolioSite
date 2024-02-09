from django import template
register = template.Library()
@register.filter
def addclass(filt, css):
    return filt.as_widget(attrs={"class":css})