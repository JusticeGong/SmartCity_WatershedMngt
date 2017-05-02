from django.db import models
from django.core.urlresolvers import reverse

class Watershed(models.Model):
    watershedID = models.CharField(max_length=20, primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=20, verbose_name='Name')
    isProtected = models.CharField(max_length=20, verbose_name='Is protected')
    percentLand = models.CharField(max_length=20, verbose_name='Percent of Land')
    supportsTourism = models.CharField(max_length=20, verbose_name='Supports Tourism')
    watershedDescription = models.CharField(max_length=255, verbose_name='Description')
    location = models.CharField(max_length=255, verbose_name='Location')

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Watershed._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:watershed_edit', kwargs={'pk': self.pk})

    class Meta:
        managed = False
        db_table = 'Watershed'
        app_label = 'watershed'



class FloraFauna(models.Model):
    florafaunaID = models.CharField(max_length=20, primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=20, verbose_name='Name')
    species = models.CharField(max_length=255, verbose_name='Species')

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in FloraFauna._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:florafauna_edit', kwargs={'florafauna_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'FloraFauna'
        app_label = 'watershed'

class ffInfo(models.Model):
    ffInfoID = models.CharField(max_length=20, primary_key=True, verbose_name='ID')
    florafaunaID = models.ForeignKey(FloraFauna, on_delete=models.CASCADE, db_column='florafaunaID', verbose_name='Flora ID')
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID', verbose_name='Watershed ID')
    isNative = models.CharField(max_length=20, verbose_name='Native')
    description = models.CharField(max_length=255, verbose_name='Description')
    photoUrl = models.CharField(max_length=1000, verbose_name='Photo URL')

    def __str__(self):
        return self.description

    class Meta:
        managed = False
        db_table = 'ffInfo'
        app_label = 'watershed'

    def attrs(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in ffInfo._meta.fields]

class Maintenance(models.Model):
    maintenanceID = models.CharField(max_length=20, primary_key=True, verbose_name='ID')
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID', verbose_name='Watershed ID')
    date = models.CharField(max_length=20, verbose_name='Date')
    issue = models.CharField(max_length=255, verbose_name='Issue')
    cost = models.CharField(max_length=255, verbose_name='Cost')
    locationofElement = models.CharField(max_length=255, verbose_name='Location')
    status = models.CharField(max_length=20, verbose_name='Status')

    def __str__(self):
        return self.issue

    def attrs(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Maintenance._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:maintenance_edit', kwargs={'maintenance_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'Maintenance'
        app_label = 'watershed'

class ManmadeFeature(models.Model):
    featureID = models.CharField(max_length=20, primary_key=True, verbose_name='ID')
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID', verbose_name='Watershed ID')
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.CharField(max_length=255, verbose_name='Description')

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in ManmadeFeature._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:manmadefeature_edit', kwargs={'feature_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'ManmadeFeature'
        app_label = 'watershed'

class NaturalFeature(models.Model):
    featureID = models.CharField(max_length=20, primary_key=True, verbose_name='ID')
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID', verbose_name='Watershed ID')
    name = models.CharField(max_length=255, verbose_name='Name')
    description = models.CharField(max_length=255, verbose_name='Description')
    latitude = models.CharField(max_length=255, verbose_name='Latitude')
    longitude = models.CharField(max_length=255, verbose_name='Longitude')

    def __str__(self):
        return self.name

    def attrs(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in NaturalFeature._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:naturalfeature_edit', kwargs={'feature_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'NaturalFeature'
        app_label = 'watershed'

class Observation(models.Model):
    observationID = models.CharField(max_length=20, primary_key=True, verbose_name='ID')
    watershedID = models.ForeignKey(Watershed, on_delete=models.CASCADE, db_column='watershedID', verbose_name='Watershed ID')
    sublocation = models.CharField(max_length=255, verbose_name='Sublocation')
    date = models.CharField(max_length=20, verbose_name='Date')
    description = models.CharField(max_length=255, verbose_name='Description')
    testType = models.CharField(max_length=20, verbose_name='Type')

    def __str__(self):
        return self.description

    def attrs(self):
        return [(field.verbose_name, field.value_to_string(self)) for field in Observation._meta.fields]

    def get_absolute_url(self):
        return reverse('watershed:observation_edit', kwargs={'observation_ID': self.pk})

    class Meta:
        managed = False
        db_table = 'Observation'
        app_label = 'watershed'


class WatershedPipe(models.Model):
    connectionID = models.CharField(max_length=20, primary_key=True, verbose_name='cID')
    watershedID = models.CharField(max_length=20, verbose_name='wID')
    pipeID = models.CharField(max_length=20, verbose_name='pID')
    class Meta:
        managed = False
        db_table = 'WatershedPipe'
        app_label = 'watershed'




