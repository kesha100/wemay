from rest_framework import serializers
from promotion.models import PromotionCategory, Promotion, Like


class PromotionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionCategory
        fields = '__all__'


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'promotion']
