from django.shortcuts import render
from django.http import HttpResponse


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
