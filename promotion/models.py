from django.db import models

from user.models import MyUser


# Create your models here.

class PromotionCategory(models.Model):
    title = models.CharField(max_length=30)
    parent_category = models.ForeignKey('self', null=True, blank=True,
                                        on_delete=models.CASCADE,
                                        related_name='subcategories')


class Promotion(models.Model):
    PROMOTION_CHOISES = (
        ('DISCOUNT', 'Скидка'),
        ('BONUS', 'Бонус'),
        ('CERTIFICATE', 'Сертификат')
    )
    category = models.ForeignKey(PromotionCategory, null=True, blank=True,
                                 on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='promotion/%Y%m%d/')
    old_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(null=True)
    description = models.TextField()
    type = models.CharField(max_length=45, choices=PROMOTION_CHOISES, default='DISCOUNT')
    contacts = models.CharField(max_length=45)
    work_time = models.CharField(max_length=25, null=True)
    address = models.CharField(max_length=85)
    likes = models.ManyToManyField(MyUser, related_name='liked_promotions')


class Like(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'promotion']
