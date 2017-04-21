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

class FloraFauna(models.Model):
    florafaunaID = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    species = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in FloraFauna._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:florafauna_edit', kwargs={'florafauna_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'FloraFauna'
        app_label = 'watershed'

class ffInfo(models.Model):
    ffInfoID = models.CharField(max_length=20, primary_key=True)
    florafaunaID = models.ForeignKey(FloraFauna, on_delete=models.CASCADE, db_column='florafaunaID')
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID')
    isNative = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    photoUrl = models.CharField(max_length=1000)

    def __str__(self):
        return self.description

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in ffInfo._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:ffInfo_edit', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'ffInfo'
        app_label = 'watershed'


class Maintenance(models.Model):
    maintenanceID = models.CharField(max_length=20, primary_key=True)
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID')
    date = models.CharField(max_length=20)
    issue = models.CharField(max_length=255)
    cost = models.CharField(max_length=255)
    locationofElement = models.CharField(max_length=255)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.issue

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in Maintenance._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:maintenance_edit', kwargs={'maintenance_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'Maintenance'
        app_label = 'watershed'

class ManmadeFeature(models.Model):
    featureID = models.CharField(max_length=20, primary_key=True)
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in ManmadeFeature._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:manmadefeature_edit', kwargs={'feature_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'ManmadeFeature'
        app_label = 'watershed'

class NaturalFeature(models.Model):
    featureID = models.CharField(max_length=20, primary_key=True)
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID')
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in NaturalFeature._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:naturalfeature_edit', kwargs={'feature_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'NaturalFeature'
        app_label = 'watershed'

class Observation(models.Model):
    observationID = models.CharField(max_length=20, primary_key=True)
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID')
    sublocation = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    testType = models.CharField(max_length=20)

    def __str__(self):
        return self.description

    def attrs(self):
        return [(field.name, field.value_to_string(self)) for field in Observation._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:observation_edit', kwargs={'observation_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'Observation'
        app_label = 'watershed'



