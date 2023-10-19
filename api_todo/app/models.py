from django.db import models

# Compreendendo os Models
    #  Representação de Dados
        # Criação de classes e seus atributes

class Todo(models.Model):
    # Attributes
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False) # Se o objeto for criado e não for passado propriedade, será atribuido como falso
    created_at = models.DateTimeField(auto_now_add=True)
    