from django.shortcuts import render
from rest_framework import generics
from promotion.models import Promotion
from .serializers import PromotionSerializer
# Create your views here.


class PromotionListAPIView(generics.ListCreateAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer


class PromotionDetailAPIView(generics.RetrieveDestroyAPIView):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer