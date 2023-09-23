# from django.db import models
from django.contrib.gis.db import models
from choices.models import EventType, City
from users.models import User


# Class that represents the eco report problem
class ReportProblem(models.Model):
    problem_type = models.CharField(choices=EventType.choices, max_length=6)
    city = models.CharField(choices=City.choices, max_length=2)
    title = models.CharField(max_length=255)
    note = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/")
    geometry = models.PointField()

    last_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
