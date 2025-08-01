from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'user']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f"{self.name} (User: {self.user_id})"

class Expense(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now, db_index=True)

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'
        ordering = ['-date']
        indexes = [
            models.Index(fields=['user', 'date']),
        ]

    def __str__(self):
        return f"{self.amount} ({self.date:%d.%m.%Y})"

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("Сумма должна быть положительной.")
        if self.date > timezone.now():
            raise ValidationError("Дата не может быть в будущем.")

    def get_absolute_url(self):
        return reverse('expense-detail', args=[str(self.id)])