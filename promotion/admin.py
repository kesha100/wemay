from django.contrib import admin
from .models import PromotionCategory, Promotion, Like
# Register your models here.


admin.site.register(PromotionCategory)
admin.site.register(Promotion)
admin.site.register(Like)