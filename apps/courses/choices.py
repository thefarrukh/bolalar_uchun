from django.db import models


class ProductTypeChoices(models.TextChoices):
    COURSE = "course", "Course"
    WEBINAR = "webinar", "Webinar"
