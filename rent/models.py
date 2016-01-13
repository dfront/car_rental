 # -*- coding: utf-8 -*-
from django.db import models
from client.models import Client
from vehicle.models import Vehicle
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.db.models import signals
from datetime import datetime
LEXERS = [item for item in get_all_lexers() if item[1]]

class Rent(models.Model):
    kmRound = models.FloatField(null=True,blank=True,default=0.0)    
    client = models.ForeignKey(Client)
    vehicle = models.ForeignKey(Vehicle)
    initialDate = models.DateTimeField()
    endDate = models.DateTimeField(null=True,blank=True)
    initialKm = models.FloatField(null=True,blank=True,default=0.0)
    endKm = models.FloatField(null=True,blank=True,default=0.0)
    thisRented = models.BooleanField(default=False)
    isReservation = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Locação"
        verbose_name_plural = "Locações"

    def vehicle_str(self):
        return self.vehicle.model.model

    def __unicode__(self):
        return self.client.name

class StatusReservation(models.Model):
    status = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Status Reserva"
        verbose_name_plural = "Status Reservas"

    def __unicode__(self):
        return self.status

class Reservation(Rent):
    status = models.ForeignKey(StatusReservation,null=True,blank=True)

    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"

    def __unicode__(self):
        return self.status.status

def reservation_post_save(sender, instance, created, **kwargs):
    if created:
        instance.status = StatusReservation.objects.get(status="nova")
        instance.isReservation = True
        instance.save()

signals.post_save.connect(reservation_post_save, sender=Reservation)

def rent_post_save(sender, instance, created, **kwargs):
    if created:
        instance.initialKm = instance.vehicle.km
        instance.thisRented = True
        instance.save()

signals.post_save.connect(rent_post_save, sender=Rent)
