from django.http import JsonResponse
from .models import Resource

def get_resources(request):
    resources = Resource.objects.all().values()
    return JsonResponse(list(resources), safe=False)