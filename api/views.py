from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from api.models import Countries
from api.serializers import *


class CountryView(APIView):

    def get(self, request):
        country_name = request.query_params.get("country")
        try:
            if country_name == "all":
                countries = Countries.objects.all()

            else:
                countries = Countries.objects.filter(title=country_name)

            serializer = CountriesSerializer(countries, many=True)
            return Response({"status": {"code": 200, "message": "success"}, "data": serializer.data},
                            status.HTTP_200_OK)

        except Countries.DoesNotExist:
            return Response({"status": {"code": 200, "message": "success"}, "data": "no records found"},
                            status.HTTP_200_OK)

