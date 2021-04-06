from django.db import models
from django.db.models.expressions import F


class Survey(models.Model):
    sex_options = (
        ('F', 'FEMININO'),
        ('M', 'MASCULINO'),
        ('O', 'OUTROS')
    )

    language_settings = (
        ('JS', 'JAVASCRIPT'),
        ('PY', 'PYTHON'),
        ('TY', 'TYPESCRIPT'),
        ('JV', 'JAVA'),
        ('C#', 'C#'),
        ('RB', 'BUBY')
    )

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    sex = models.CharField(
        max_length=1, choices=sex_options, blank=False, null=False)
    language = models.CharField(
        max_length=2, choices=language_settings, blank=False, null=False)
    description = models.TextField()
    active = models.BooleanField(default=True)
    begin_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
