from django.db import models
from django.core.urlresolvers import reverse

class Watershed(models.Model):
    watershedID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    #isProtected = models.CharField(max_length=20)
    percentLand = models.CharField(max_length=20)
    supportsTourism = models.CharField(max_length=20)
    watershedDescription = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('watershed:index')

    def __str__(self):
        return self.name

class ffInfo(models.Model):
    florafaunaID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    isNative = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    photoUrl = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class FloraFauna(models.Model):
    florafaunaID = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    species = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Maintenance(models.Model):
    maintenanceID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    date = models.CharField(max_length=20)
    issue = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    locationofElement = models.CharField(max_length=255)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.issue

class ManmadeFeature(models.Model):
    featureID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class NaturalFeature(models.Model):
    featureID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Observation(models.Model):
    observationID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    sublocation = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    testType = models.CharField(max_length=20)

    def __str__(self):
        return self.description


