from django import template
register = template.Library()

@register.inclusion_tag('custom_admin/table_tools.html')
def table_tools():
    return {}