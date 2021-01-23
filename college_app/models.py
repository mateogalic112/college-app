from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Korisnik(AbstractUser):
    MENTOR = 'MENTOR'
    STUDENT = 'STUDENT'
    ROLES = (
        (MENTOR, 'Mentor'),
        (STUDENT, 'Student'),
    )

    NONE = 'NONE'
    REDOVNI = 'REDOVNI'
    IZVANREDNI = 'IZVANREDNI'
    STATUS = (
        (NONE, 'None'),
        (REDOVNI, 'Redovni'),
        (IZVANREDNI, 'Izvanredni'),
    )
    role = models.CharField(
        max_length=12,
        choices=ROLES,
        default=STUDENT,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default=NONE,
    )

class Predmet(models.Model):
    DA = 'DA'
    NE = 'NE'
    IZBORNI = (
        (DA, 'Da'),
        (NE, 'Ne'),
    )
    ime = models.CharField(max_length=100)
    kod = models.CharField(max_length=6)
    program = models.TextField(null=False)
    bodovi = models.IntegerField(null=False)
    sem_redovni = models.IntegerField(null=False)
    sem_izvanredni = models.IntegerField(null=False)
    izborni = models.CharField(max_length=2, choices=IZBORNI)




