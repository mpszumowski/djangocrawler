from django.db import models


class Countries(models.Model):
    """A list of countries scraped from the World Bank DB"""
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"

    def __str__(self):
        return self.name

    @classmethod
    def all_countries(cls):
        countries = cls.objects.all()
        return countries


class CountryMixin(models.Model):
    """Links each model containing data with the list of countries"""
    country = models.ForeignKey(Countries, on_delete=True)

    class Meta:
        abstract = True


class DateScrapedMixin(models.Model):
    """Adds info about the date of scraping the data"""
    date_scraped = models.DateField()

    class Meta:
        abstract = True


class MinimumAmount(CountryMixin,
                    DateScrapedMixin):
    """The minimum amount of $ per 2400kcal per day in each country"""
    amount = models.CharField(max_length=16)


class PovertyPercent(CountryMixin,
                     DateScrapedMixin):
    """The % of people living under $3.10 per day"""
    percent = models.CharField(max_length=16)
    data_year = models.CharField(max_length=16, null=True)


class CountryPopulation(CountryMixin,
                        DateScrapedMixin):
    """Population in millions"""
    estimate = models.CharField(max_length=32)
    data_year = models.CharField(max_length=16, null=True)


class Misfits(DateScrapedMixin):
    """This model fetches all the data that is scraped and which
    in the course of processing by Scrapy does not fit any key
    from the base model Countries. This model is for control
    and debugging purposes."""
    name = models.CharField(max_length=64)
    minimum_amount = models.CharField(max_length=32, null=True)
    minimum_amount_year = models.CharField(max_length=16, null=True)
    percent = models.CharField(max_length=16, null=True)
    percent_year = models.CharField(max_length=16, null=True)
    population_estimate = models.CharField(max_length=32, null=True)
    population_year = models.CharField(max_length=16, null=True)
