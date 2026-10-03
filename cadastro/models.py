from django.db import models


class Pessoa(models.Model):
    nome = models.CharField('nome', max_length=100)
    email = models.EmailField('e-mail', unique=True)
    idade = models.PositiveSmallIntegerField('idade')

    class Meta:
        ordering = ['nome']
        verbose_name = 'pessoa'
        verbose_name_plural = 'pessoas'

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, related_name='telefones')
    numero = models.CharField('número', max_length=20)

    class Meta:
        verbose_name = 'telefone'
        verbose_name_plural = 'telefones'

    def __str__(self):
        return self.numero
