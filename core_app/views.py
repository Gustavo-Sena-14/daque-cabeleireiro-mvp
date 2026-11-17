from django.http import JsonResponse
from django.db import IntegrityError
from .models import Cliente, Agendamento

def reservar_horario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        whatsapp = request.POST.get('whatsapp')
        data_hora = request.POST.get('data_hora')
        servico = request.POST.get('servico')
        cliente, _ = Cliente.objects.get_or_create(whatsapp=whatsapp, defaults={'nome': nome})
        try:
            Agendamento.objects.create(cliente=cliente, data_hora=data_hora, servico=servico)
            return JsonResponse({'status': 'sucesso'})
        except IntegrityError:
            return JsonResponse({'status': 'erro'}, status=400)
    return JsonResponse({'status': 'erro'}, status=405)