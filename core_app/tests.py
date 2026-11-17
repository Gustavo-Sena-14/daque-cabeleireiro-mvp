import pytest
from django.test import Client
from core_app.models import Cliente, Agendamento

@pytest.mark.django_db
def test_reserva_sucesso():
    client = Client()
    response = client.post('/reservar/', {
        'nome': 'João Silva', 'whatsapp': '11999999999', 
        'data_hora': '2026-11-20 14:30:00', 'servico': 'Corte'
    })
    assert response.status_code == 200

@pytest.mark.django_db
def test_falha_double_booking():
    Cliente.objects.create(nome="Maria", whatsapp="11888888888")
    client = Client()
    client.post('/reservar/', {'nome': 'Maria', 'whatsapp': '11888888888', 'data_hora': '2026-11-20 15:00', 'servico': 'Corte'})
    
    response_falha = client.post('/reservar/', {'nome': 'Pedro', 'whatsapp': '11777777777', 'data_hora': '2026-11-20 15:00', 'servico': 'Barba'})
    assert response_falha.status_code == 400