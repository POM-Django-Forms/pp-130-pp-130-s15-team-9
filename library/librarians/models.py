from django.db import models

class Librarian(models.Model):
    імʼя = models.CharField(max_length=100)
    прізвище = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    телефон = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.імʼя} {self.прізвище}"
