# -*- coding: utf-8 -*-
from django import forms
from datetime import datetime

class RentForm(forms.Form):
    initialDate = forms.DateTimeField(label="Data Inicial",
                                    input_formats="%d/%m/%y %H:%M",
                                    widget=forms.TextInput(attrs={'class':'form-control'}))
    endDate = forms.DateTimeField(label="Data Final",
                                  input_formats="%d/%m/%y %H:%M", 
                                  widget=forms.TextInput(attrs={'class':'form-control'}))
