from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dojos(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    desc = models.TextField(blank=True)

class Ninjas(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id = models.ForeignKey(Dojos, related_name="ninjas")

COMMANDS:
Dojos.objects.create(name="CodingDojo Silicon Valley", city="Mountain View", state="CA")
Dojos.objects.create(name="CodingDojo Seattle", city="Seattle", state="WA")
Dojos.objects.create(name="CodingDojo New York", city="New York", state="NY")
Dojos.objects.get(id=1).delete()
Dojos.objects.get(id=2).delete()
Dojos.objects.get(id=3).delete()
Dojos.objects.create(name="CodingDojo San Diego", city="San Diego", state="CA")
Dojos.objects.create(name="CodingDojo Olympia", city="Olympia", state="WA")
Dojos.objects.create(name="CodingDojo Boston", city="Boston", state="MA")
Ninjas.objects.create(first_name="Anna", last_name="C", dojo_id=Dojos.objects.get(id=4))
Ninjas.objects.create(first_name="Eric", last_name="L", dojo_id=Dojos.objects.get(id=4))
Ninjas.objects.create(first_name="Marc", last_name="L", dojo_id=Dojos.objects.get(id=4))
Ninjas.objects.create(first_name="Caitlin", last_name="S", dojo_id=Dojos.objects.get(id=5))
Ninjas.objects.create(first_name="Dan", last_name="O", dojo_id=Dojos.objects.get(id=5))
Ninjas.objects.create(first_name="Jan", last_name="O", dojo_id=Dojos.objects.get(id=5))
Ninjas.objects.create(first_name="Mo", last_name="H", dojo_id=Dojos.objects.get(id=6))
Ninjas.objects.create(first_name="Jack", last_name="L", dojo_id=Dojos.objects.get(id=6))
Ninjas.objects.create(first_name="Mo", last_name="H", dojo_id=Dojos.objects.get(id=6))
Ninjas.objects.filter(dojo_id = Dojos.objects.first())
Ninjas.objects.filter(dojo_id = Dojos.objects.last())
exit #add desc text field to class in models.py
python manage.py makemigrations
python manage.py migrate
python manage.py shell
from apps.dojos_ninjas.models import *
