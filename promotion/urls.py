from django.urls import path
from promotion.api.views import PromotionListAPIView, PromotionDetailAPIView
urlpatterns = [
    path('promotion/', PromotionListAPIView.as_view(), name='promotion'),
    path('promotion/<int:pk>/', PromotionDetailAPIView.as_view(), name='promotion-detail')
]