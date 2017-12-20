from rest_framework import serializers
from .models import (Countries, CountryPopulation, MinimumAmount,
                     PovertyPercent)


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields = ("name", )


class PopulationSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="countries.name")

    class Meta:
        model = CountryPopulation
        fields = ("country", "estimate", "data_year", "data_scraped")


class MinimumAmountSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="countries.name")

    class Meta:
        model = MinimumAmount
        fields = ("country", "amount", "data_scraped")


class PovertyPercentSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="countries.name")

    class Meta:
        model = PovertyPercent
        fields = ("country", "percent", "data_year", "data_scraped")
