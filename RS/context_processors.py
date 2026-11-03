from django.core.cache import cache
from .models import RedSocial

def redes_sociales(request):
    modelos = cache.get('modelos_footer_cache')
    if not modelos:
        modelos = list(RedSocial.objects.all())
        cache.set('modelos_footer_cache', modelos, 60 * 15)
    return {'redessociales': modelos}