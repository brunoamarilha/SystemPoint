from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def ver_ponto(request): 
    if request.method == "GET":
    
        return render(request, 'ponto.html', )
    elif request.method == "POST":
        hr_entrada = request.POST.get('entrada')
        hr_saida = request.POST.get('saida')
        desc = request.POST.get('descricao')

        try:
            # O formato esperado é 'HH:MM' para horas
            hr_entrada = datetime.strptime(hr_entrada, '%H:%M').time()
            hr_saida = datetime.strptime(hr_saida, '%H:%M').time()

            # Exibe as horas e a descrição
            print(f'Entrada: {hr_entrada}, Saída: {hr_saida}, Descrição: {desc}')
            return HttpResponse('Informação recebida com sucesso!')
        
        except ValueError as e:
            return HttpResponse(f'Erro ao processar os horários: {e}')

def inserir_ponto(request):
    return HttpResponse('Inserir ponto')