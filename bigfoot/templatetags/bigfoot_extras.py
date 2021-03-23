from django import template
from django.core.cache import cache

register = template.Library()

@register.filter(name='user_activity_text')
def user_activity_text(user):
    cache_key = f'user_activity_text_{user.id}'
    comment_count = cache.get(cache_key)
    if comment_count is None:
        comment_count = user.get_recent_comments_count()
        cache.set(cache_key, comment_count, 3600)

    if (comment_count > 50):
        return 'bigfoot fanatic'
    elif (comment_count > 30):
        return 'believer'
    elif (comment_count > 20):
        return 'hobbyist'

    return 'skeptic'
