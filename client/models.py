 # -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class CnhCategory(models.Model):
    category = models.CharField(max_length=1)
    description = models.TextField(null=True,blank=True)

    class Meta:
        verbose_name = "CHN Categories"
        verbose_name_plural = "Categoria CHN"

    def __unicode__(self):
        return self.category

class Client(models.Model):
    user = models.OneToOneField(User,blank=True,null=True,unique=True,related_name="profile")
    name = models.CharField(max_length=255)
    cpf = models.IntegerField()
    cnhNumber = models.IntegerField(null=True,blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __unicode__(self):
        return self.name

class ClientCnhCategory(models.Model):
    client = models.ForeignKey(Client)
    category = models.ForeignKey(CnhCategory)

    class Meta:
        verbose_name = "Cliente Categoria CNH"
        verbose_name_plural = "Clientes Categorias CNH"

    def __unicode__(self):
        return self.category.category
