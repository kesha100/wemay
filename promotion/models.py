from django.db import models

# Create your models here.


class Promotion(models.Model):
    PROMOTION_CHOISES = (
        ('DISCOUNT', 'Скидка'),
        ('BONUS', 'Бонус'),
        ('CERTIFICATE', 'Сертификат')
    )
    title = models.CharField(max_length=25)
    image = models.ImageField(upload_to='promotion/%Y/%m/%d')
    description = models.TextField()
    type = models.CharField(max_length=45, choices=PROMOTION_CHOISES, default='DISCOUNT')
    price = models.PositiveIntegerField()
    contacts = models.CharField(max_length=45)
    address = models.CharField(max_length=85)