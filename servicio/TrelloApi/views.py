from django.shortcuts import render
import json
import requests
from django.http import HttpResponse

# Create your views here.

def Tableros(request):
    apikeytrello = 'eab7d0f6391a2f299508d302ef0be11a'
    token_trello = 'd38b99bbbfbe3f2401a5b02f1a52fb8f51ab87021eaf9eccab639883342d867e'
    url = 'https://api.trello.com/1/members/me/boards?key=' + apikeytrello + '&token=' + token_trello
    response = requests.request("GET", url)
    r = response.status_code
    respuesta = response.json()

    s = '['
    commaCount = 0
    for xx in respuesta:
        s = s + '{'
        s = s + '"nombre":' + '"' + xx["name"] + '"' + ','
        s = s + '"id":' + '"' + xx['id'] + '"'
        commaCount = commaCount + 1
        if commaCount < len(respuesta):
            s = s + '},'
    s = s + '}]'

    respuestaHtml=s
    respuestaJson = json.loads(respuestaHtml)


    return HttpResponse(respuestaHtml)

