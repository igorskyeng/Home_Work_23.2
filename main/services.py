from django.conf import settings
from django.core.cache import cache

from main.models import Category


def get_date_from_cache(context_data, model, title=''):
    if settings.CACHE_ENABLED:
        key = f'object_list_{model.objects.all()}'
        object_list = cache.get(key)

        if object_list is None:
            object_list = model.objects.all()
            cache.set(key, object_list)

    else:
        object_list = model.objects.all()

    context_data['object_list'] = object_list
    context_data['title'] = title

    return context_data
