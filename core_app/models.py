from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    whatsapp = models.CharField(max_length=20, unique=True)

class Agendamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()
    servico = models.CharField(max_length=50)

    class Meta:
        unique_together = ('data_hora',)