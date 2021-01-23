from django.contrib import admin

from .models import Korisnik, Predmet

# Register your models here.
admin.site.register(Korisnik)
admin.site.register(Predmet)

