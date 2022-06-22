from django.shortcuts import render

from django.http import HttpResponse, JsonResponse


def index(request):
  if request.method == 'POST':
    return HttpResponse("Hello, world. You're at the polls index.")
  elif request.method =='GET':
    return JsonResponse({'teste': 'teste'})