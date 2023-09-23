from django.db import models


# Create your models here.

class City(models.TextChoices):
    Doboj = ("DO", "Doboj")
    Banja_Luka = ("BL", "Banja Luka")
    Bijeljina = ("BJ", "Bijeljina")
    Istocno_Sarajevo = ("IS", "Istocno Sarajevo")


class EventType(models.TextChoices):
    Zastita_vazduha_i_ozonskog_omotaca = ("ZVIOO", "Zastita vazduha i ozonskog omotaca")
    Zastita_vode = ("ZVODE", "Zastita vode")
    Zastita_zivotne_sredine = ("ZZS", "Zastita zivotne sredine")
    Zastita_od_buke_i_vibracije = ("ZBIV", "Zastita od buke i vibracije")
    Zastita_zemljista = ("ZZ", "Zastita zemljista")
    Zasticena_podrucja = ("ZP", "Zasticena podrucja")
    Zasticene_vrste = ("ZVRSTE", "Zasticene vrste")
    Ribolovne_vode = ("RV", "Ribolovne vode")
    Upravljanje_otpadom = ("UO", "Upravljanje otpadom")
    Hemijski_udesi = ("HU", "Hemijski udesi")
