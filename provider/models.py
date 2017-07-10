from django.db import models


class ProviderType(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    defined_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    provider_type = models.ForeignKey(ProviderType)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    provider = models.ForeignKey(Provider)

    def __str__(self):
        return self.name
