from django.shortcuts import render
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from datetime import datetime
from .models import Register
from .models import Point


def ver_ponto(request): 
    if request.method == "GET":
        return render(request, 'ponto.html')

    elif request.method == "POST":
        hr_join = request.POST.get('entrada')  # Captura a entrada do formulário
        hr_exit = request.POST.get('saida')    # Captura a saída do formulário
        desc = request.POST.get('descricao')   # Captura a descrição do formulário

        try:
            # Verifica se os horários foram recebidos corretamente
            if hr_join and hr_exit:
                hr_entrada = datetime.strptime(hr_join, '%H:%M').time()  # Converte a entrada
                hr_saida = datetime.strptime(hr_exit, '%H:%M').time()    # Converte a saída

                # Cria e salva o ponto
                point = Point(point_id=get_random_string(length=10), hr_join=hr_entrada, hr_exit=hr_saida, desc=desc)
                point.save()

                print(f'Entrada: {hr_entrada}, Saída: {hr_saida}, Descrição: {desc}')
                return HttpResponse('Informação recebida com sucesso!')
            else:
                return HttpResponse('Horários de entrada e saída são obrigatórios.')
        
        except ValueError as e:
            return HttpResponse(f'Erro ao processar os horários: {e}')



def menu(request): 
    if request.method == "GET":
        return render(request, 'menu.html')