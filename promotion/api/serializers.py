from rest_framework import serializers
from promotion.models import Promotion


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'title', 'image', 'description', 'type', 'price', 'contacts', 'address']
