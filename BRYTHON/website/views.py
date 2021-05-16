from django.shortcuts import render
from django.http import JsonResponse
from pegar_cep import CEP

def index(request):
    return render(request, 'index.html')

def ajaxme(request):
    data = {'dados': CEP(request.POST.get('cep'), '').pegar_endereco()}
    return JsonResponse(data, status=200)