import requests
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render

class Apiexterna(View):
    def get(self, request):
        response = requests.get(
            'https://deckofcardsapi.com/api/deck/new/draw/?count=2',
        )
        dados = response.json()
        return JsonResponse(dados)