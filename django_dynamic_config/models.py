from django.db import models

# Create your models here.

VALUE_TYPE_CHOICES = (
    ("int", "Int"),
    ("float", "Float"),
    ("str", "String"),
    ("bool", "Boolean"),
    ("json", "JSON")
)
VALUE_TYPE_LIST = [_type for _type, _ in VALUE_TYPE_CHOICES]


class DynamicConfig(models.Model):
    key = models.CharField("Key", unique=True, max_length=32)
    value = models.TextField("Value")
    value_type = models.CharField("Value Type", max_length=12, choices=VALUE_TYPE_CHOICES)
    is_show = models.BooleanField("Whether the API returns.", default=True)
    desc = models.CharField("Description about this field", max_length=128, null=True)
