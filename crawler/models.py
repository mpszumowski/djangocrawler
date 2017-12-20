import json
from django.db import models


class MinimumAmount(models.Model):
    country = models.CharField(max_length=128)
    amount = models.CharField(max_length=16)

    @property
    def to_dict(self):
        data = {
            "country": json.loads(self.country),
            "amount": json.loads(self.amount)
        }
        return data

    def __str__(self):
        return self.country


class PovertyPercent(models.Model):
    country = models.CharField(max_length=128)
    percent = models.CharField(max_length=16)