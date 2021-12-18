from django.template import Library, context

register = Library()
@register.inclusion_tag('pagination.html')
def pagination(request, paginator, page_obj):
    context = {}
    context['paginator'] = paginator
    context['request'] = request
    context['page_obj'] = page_obj
    get_vars = request.GET.copy()
    if 'page' in get_vars:
        del get_vars['page']
    if len(get_vars) > 0:
        context['getvars'] = '&{0}'.format(get_vars.urlencode())
    else:
        context['getvars'] = ''
    return context