from django.db import models
import csv

# Create your models here.
class WineInfo(models.Model):
    name = models.CharField(max_length=100)
    cat = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    def read_csv(self):
        with open('/home/pirl/posco_Ai_Bigdata/wineproject/home/static/winename.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # The header row values become your keys
                name = row['name']
                cat = row['cat']
                model = self(name=name, cat=cat)
                model.save()
