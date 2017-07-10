from django.db import models


class Zone(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    zone = models.ForeignKey(Zone)


class State(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    country = models.ForeignKey(Country)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    state = models.ForeignKey(State)

    def __str__(self):
        return self.name


class LGA(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    region = models.ForeignKey(Region)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    state = models.ForeignKey(State)


class Symptom(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class MedicalProcedure(models.Model):
    name = models.TextField()
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name[0:50]


class Drug(models.Model):
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=50)
    procedures = models.ManyToManyField(MedicalProcedure)

    def __str__(self):
        return self.name


class Disease(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    symptoms = models.ManyToManyField(Symptom)
    drugs = models.ManyToManyField(Drug)
    procedures = models.ManyToManyField(MedicalProcedure)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class ProductPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=30, decimal_places=4)
    validity = models.CharField(max_length=50)
    age_group = models.CharField(max_length=30)  # We should actually create choices for this.
    valid_from = models.DateTimeField()
    valid_till = models.DateTimeField()
