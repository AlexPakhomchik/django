from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    host = request.META['HTTP_HOST']
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path
    return HttpResponse(f'''
        <p>Host:{host}</p>
        <p>User-Agent:{user_agent}</p>
        <p>Path:{path}</p>
    ''', headers={'money':127})


def first_page(request, name, place):
    return HttpResponse(f'''
    <p>Name:{name}</p>
    <p>Place:{place}</p>
    ''')


def second_page(requests, santa='undefined', place='antarctic'):
    return HttpResponse(f'Santa say: {santa} and fly to the {place}')


def json_example(request):
    return JsonResponse({'USD': 2.60, 'EUR': 2.80})


def set_cookie(request):
    username = request.GET.get('username', 'undefined')
    response = HttpResponse(f'Hi, {username}')
    response.set_cookie('username', username)
    return response


def get_cookie(request):
    username = request.COOKIES['username']
    return HttpResponse(f'Hi, {username}')
