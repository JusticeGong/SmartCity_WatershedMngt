from django.db import models
from django.core.urlresolvers import reverse

class Watershed(models.Model):
    watershedID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    isProtected = models.CharField(max_length=20)
    percentLand = models.CharField(max_length=20)
    supportsTourism = models.CharField(max_length=20)
    watershedDescription = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in Watershed._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:watershed_edit', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'Watershed'
        app_label = 'watershed'

class ffInfo(models.Model):
    florafaunaID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    isNative = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    photoUrl = models.CharField(max_length=100)

    def __str__(self):
        return self.description

class FloraFauna(models.Model):
    florafaunaID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    species = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in FloraFauna._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:florafauna_edit', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'FloraFauna'
        app_label = 'watershed'

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

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in Maintenance._meta.fields]

class ManmadeFeature(models.Model):
    featureID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in ManmadeFeature._meta.fields]

class NaturalFeature(models.Model):
    featureID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in NaturalFeature._meta.fields]

class Observation(models.Model):
    observationID = models.CharField(max_length=20)
    watershedID = models.CharField(max_length=20)
    sublocation = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    testType = models.CharField(max_length=20)

    def __str__(self):
        return self.description

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in Observation._meta.fields]



