from django.db import models

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'A Fazer'),
        ('DOING', 'Em Andamento'),
        ('DONE', 'Concluído'),
    ]

    titulo = models.CharField(max_length=200, help_text="Título da demanda")
    descricao = models.TextField(blank=True, null=True, help_text="Detalhes ou briefing")
    tags = models.CharField(max_length=255, blank=True, null=True, help_text="Ex: Urgente, Instagram")
    prazo = models.DateTimeField(help_text="Data limite")
    status = models.CharField(max_length=5, choices=STATUS_CHOICES, default='TODO')
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.status})"
    
    class Meta:
        ordering = ['prazo']