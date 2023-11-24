from rest_framework import serializers
from api.models import Countries, Places


class CountriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Countries
        fields = ['title', 'body', 'created', 'image']


class PlacesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Places
        fields = ['title', 'description', 'created', 'image']
