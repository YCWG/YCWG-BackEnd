from django.db import models


FOOD_CATEGORY = (
    ('족발,보쌈','패스트푸드','아시안','찜,탕,찌개','카페,디저트',
    '백반,죽,국수','중식','도시락','피자','돈까스,회,일식','양식','고기,구이','분식','치킨')
)

class Party(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=24)
    place = models.CharField(max_length=255)
    member_limit = models.IntegerField(max_length=50)
    date = models.DateTimeField()
    description = models.TextField(blank=True)
