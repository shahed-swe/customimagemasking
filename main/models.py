from django.db import models

# Create your models here.
class MaskCategory(models.Model):
    category_name = models.CharField(max_length=120)
    mask_image = models.ImageField(upload_to="mask/")

    class Meta:
        db_table = "mask_category"

    def __str__(self):
        return f"{self.category_name[0: 5]} -> {self.pk}"

