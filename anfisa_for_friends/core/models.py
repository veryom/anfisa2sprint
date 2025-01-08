from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добвляет флаги is_published и title."""
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубиковано'
    )

    class Meta:
        abstract = True
