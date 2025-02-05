from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.utils.timezone import now

def api_view(request):
  return JsonResponse({
    'email': "awetheophiluso.1@gmail.com",
    'current_datetime': now().isoformat(),
    'github_url': 'https://github.com/theophilusawe/st-zero'
  })
