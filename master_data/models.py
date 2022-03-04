from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = '01 Category'

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, related_name='subcategory', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = '02 Sub Category'

    def __str__(self):
        return self.name
