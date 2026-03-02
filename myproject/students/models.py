from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
        models.CheckConstraint(
            condition=models.Q(age__lte=100),
            name="age_lte_100"
        )
    ]
    def __str__(self):
        return self.name