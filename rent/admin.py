# -*- coding: utf-8 -*-
from django.contrib import admin
from rent.models import Rent, StatusReservation, Reservation
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django import forms
from datetime import datetime

def makeReservation(modeladmin,request,queryset):
    for obj in queryset: 
        obj.thisRented=True
        obj.isReservation=False
        obj.initialKm = obj.vehicle.km
        obj.status=StatusReservation.objects.get(status="efetivada")
        obj.save()

makeReservation.short_description = "Efetivar locação"

def cancelReservation(modeladmin,request,queryset):
    queryset.update(status=StatusReservation.objects.get(status="cancelada"))

cancelReservation.short_description = "Cancelar locação"


class RentAdmin(admin.ModelAdmin):
    list_display = ("client","vehicle","initialDate","endDate","initialKm","endKm","kmRound","thisRented","isReservation")
    exclude = ("endDate","endKm","initialKm","thisRented","kmRound","isReservation")
    

    class DevolutionForm(forms.Form):
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
        kmRound=forms.FloatField()

    def makeDevolution(self,request,queryset):
        form = None
        c = {}
        if "makeDevolution" in request.POST:
            form = self.DevolutionForm(request.POST)
            if form.is_valid():
                kmRound = form.cleaned_data['kmRound']
                for rent in queryset:
                    rent.kmRound = kmRound
                    rent.thisRented = False
                    rent.endDate = datetime.today()
                    rent.endKm += rent.initialKm + kmRound
                    rent.vehicle.km += kmRound
                    rent.vehicle.save()
                    rent.save()

                self.message_user(request,"Operação realizada com sucesso.")
                return HttpResponseRedirect(request.get_full_path())

        if not form:
            form = self.DevolutionForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

        c.update({'queryset': queryset, 'form': form })
        c.update(csrf(request))
        return render_to_response('admin/makeDevolution.html', c)

    makeDevolution.short_description = "Realizar Devolução"
    actions = [makeDevolution,]

class ReservationAdmin(admin.ModelAdmin):
    list_display = ("client","vehicle","initialDate","status")
    exclude = ("endDate","endKm","initialKm","thisRented","kmRound","isReservation","status")
    actions = [makeReservation,cancelReservation]

admin.site.register(Rent,RentAdmin)
admin.site.register(StatusReservation)
admin.site.register(Reservation,ReservationAdmin)
