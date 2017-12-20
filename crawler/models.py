from django.db import models


class Countries(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class MinimumAmount(models.Model):
    country = models.ForeignKey(Countries, on_delete=True)
    amount = models.CharField(max_length=16)
    date_scraped = models.DateField()


class PovertyPercent(models.Model):
    country = models.ForeignKey(Countries, on_delete=True)
    percent = models.CharField(max_length=16)
    data_year = models.CharField(max_length=16, null=True)
    date_scraped = models.DateField()


class CountryPopulation(models.Model):
    country = models.ForeignKey(Countries, on_delete=True)
    estimate = models.CharField(max_length=32)
    data_year = models.CharField(max_length=16, null=True)
    date_scraped = models.DateField()


class Misfits(models.Model):
    name = models.CharField(max_length=64)
    minimum_amount = models.CharField(max_length=32, null=True)
    minimum_amount_year = models.CharField(max_length=16, null=True)
    percent = models.CharField(max_length=16, null=True)
    percent_year = models.CharField(max_length=16, null=True)
    population_estimate = models.CharField(max_length=32, null=True)
    population_year = models.CharField(max_length=16, null=True)
    date_scraped = models.DateField()
