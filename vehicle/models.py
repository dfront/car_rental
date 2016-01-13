 # -*- coding: utf-8 -*-
from django.db import models
from client.models import CnhCategory


class VehicleCategory(models.Model):
    category = models.CharField(max_length=255)
    cnhCategoryPermited = models.ForeignKey(CnhCategory)

    class Meta:
        verbose_name = "Categoria veiculo"
        verbose_name_plural = "Categorias veiculos"

    def __unicode__(self):
        return self.category

class VehicleModel(models.Model):
    model = models.CharField(max_length=255)
    category = models.ForeignKey(VehicleCategory)

    class Meta:
        verbose_name = "Modelo veiculo"
        verbose_name_plural = "Modelos veiculos"

    def __unicode__(self):
        return self.model

class Vehicle(models.Model):
    category = models.ForeignKey(VehicleCategory)
    model = models.ForeignKey(VehicleModel)
    km  = models.FloatField()
    board = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Veiculo"
        verbose_name_plural = "Veículos"

    def __unicode__(self):
        return  self.model.model + " - Placa: " + self.board
