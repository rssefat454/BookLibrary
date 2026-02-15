from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    class CategoryChoices(models.TextChoices):
        FICTION = 'Fiction', _('Fiction')
        SCIFI = 'Sci-Fi', _('Sci-Fi')
        HISTORY = 'History', _('History')
        COMIC = 'Comic', _('Comic')
        OTHER = 'Other', _('Other')

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CategoryChoices.choices)
    published_date = models.DateField()
    status = models.BooleanField(default=True)  # True = Available, False = Borrowed
    image = models.ImageField(upload_to='books/', blank=True, null=True)

    def __str__(self):
        return self.title
