from django.db import models

# Formulário de cadastro de livro:

class Book(models.Model):
    created_at=models.DateTimeField(auto_now_add=True) # data de criação do casdastro.
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    year=models.IntegerField()
    genre=models.CharField(max_length=30)
    value=models.FloatField()

    def __str__(self): # Função para retornar uma mensagem espefícia ao inves de mensagens da memória.
        return (f'{self.title}- {self.value}')
    
    #Após a criação da tabela, executar o makemigrate e migrate para criar a tabela no banco de dados