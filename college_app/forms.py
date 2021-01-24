from django.forms import ModelForm

from .models import *

class EnrollForm(ModelForm):
    class Meta:
        model = Enroll
        fields = ['status']