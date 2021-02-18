from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def test(request):
    data = {'name':'taiwo', 'age': 23 }
    return JsonResponse(data);