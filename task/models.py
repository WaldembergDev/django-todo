from django.db import models
from django.utils import timezone
from account.models import User

class StatusEnum(models.TextChoices):
    PENDING = 'Pendente'
    IN_PROGRESS = 'Andamento'
    FINISHED = 'Finalizada'

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=20,
                               choices=StatusEnum.choices,
                                 default=StatusEnum.PENDING)
    
    def __str__(self):
        return self.name