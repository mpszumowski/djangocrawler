from rest_framework import serializers
from .models import (Countries, CountryPopulation, MinimumAmount,
                     PovertyPercent)


class PopulationSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="countries.name")

    class Meta:
        model = CountryPopulation
        fields = ("country", "estimate", "data_year", "date_scraped")


class MinimumAmountSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="countries.name")

    class Meta:
        model = MinimumAmount
        fields = ("country", "amount", "date_scraped")


class PovertyPercentSerializer(serializers.HyperlinkedModelSerializer):
    country = serializers.ReadOnlyField(source="countries.name")

    class Meta:
        model = PovertyPercent
        fields = ("country", "percent", "data_year", "date_scraped")


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    population = PopulationSerializer(source="countrypopulation_set",
                                      many=True,
                                      read_only=True)
    poverty = PovertyPercentSerializer(source="povertypercent_set",
                                       many=True,
                                       read_only=True)
    amount = MinimumAmountSerializer(source="minimumamount_set",
                                     many=True,
                                     read_only=True)
    class Meta:
        model = Countries
        fields = ("name", "population", "poverty", "amount")

