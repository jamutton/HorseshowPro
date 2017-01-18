from django import forms
from django.forms import ModelForm
from models import *

class RiderForm(ModelForm):
    class Meta:
        model = Rider
        fields = '__all__'

class ClassResultsForm(ModelForm):
    class Meta:
        model = ClassEntry
        fields = '__all__'

class JudgingForm(ModelForm):
    class Meta:
        model = Judging
        fields = '__all__'
