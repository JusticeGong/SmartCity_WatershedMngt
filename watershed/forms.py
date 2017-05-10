from django import forms
from watershed.models import *


# ----------Watershed Forms --------
class WatershedForm(forms.ModelForm):
    #Fields
    watershedID = forms.CharField(max_length=128, label="Please enter ID:", widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=20, label="Enter the name of the watershed:", widget=forms.TextInput(attrs={'class':'form-control'}))
    isProtected = forms.ChoiceField(label="Is it protected?", choices=[('Yes','yes'),('No', 'no')], widget=forms.Select(attrs={'class':'form-control'}))
    percentLand = forms.CharField(max_length=20, label="percentage of land:", widget=forms.TextInput(attrs={'class':'form-control'}))
    supportsTourism = forms.ChoiceField(label="Does it support Tourism?", choices=[('Yes','yes'),('No', 'no')], widget=forms.Select(attrs={'class':'form-control'}))
    watershedDescription = forms.CharField(max_length=255, label="Description:", widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))
    latitude = forms.CharField(max_length=20, label="What is its latitude",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitude = forms.CharField(max_length=20, label="What is its longitude?",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Watershed
        exclude = []


# ----------Maintenance Forms ------
class MaintenanceForm(forms.ModelForm):
    #Variables
    possibleStatus = [('In progress', 'In progress'),('Complete', 'Complete'),('Opened', 'Opened')] #value, lable

    #Fields
    date = forms.CharField(max_length=20, label="Date of issue:", widget=forms.TextInput(attrs={'class':'form-control'}))
    cost = forms.CharField(max_length=20, label="Costs:", widget=forms.TextInput(attrs={'class':'form-control'}))
    locationofElement = forms.CharField(max_length=20, label="Where is it located?", widget=forms.TextInput(attrs={'class':'form-control'}))
    issue = forms.CharField(max_length=255, label="Issue:", widget=forms.TextInput(attrs={'class':'form-control'}))
    status = forms.ChoiceField(choices=possibleStatus, label="Current status:", widget=forms.Select(attrs={'class':'form-control'}))
    maintenanceID = forms.CharField(max_length=20, label="ID:", widget=forms.TextInput(attrs={'class':'form-control'}))
    watershedID = forms.ModelChoiceField(label='Relation to Watershed', queryset=Watershed.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Maintenance
        exclude = []

#------------ Flora and Fauna ------
class FloraFaunaForm(forms.ModelForm):

    florafaunaID = forms.CharField(max_length=20, label="ID:", widget=forms.TextInput(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=20, label="Name:", widget=forms.TextInput(attrs={'class':'form-control'}))
    species = forms.CharField(max_length=255, label="Specie:", widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = FloraFauna
        exclude=[]

#------------ffInfo????
class ffInfoForm(forms.ModelForm):
    ffInfoID = forms.CharField(max_length=20, label="ID:", widget=forms.TextInput(attrs={'class':'form-control'}))
    watershedID = forms.ModelChoiceField(label='Relation to Watershed', queryset=Watershed.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    florafaunaID = forms.ModelChoiceField(label='Relation to Flora', queryset=FloraFauna.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    isNative = forms.ChoiceField(label="Is it native?", choices=[('Yes','yes'),('No', 'no')], widget=forms.Select(attrs={'class':'form-control'}))
    photoUrl = forms.CharField(max_length=255, label="Phot URL:", widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=255, label="Description:", widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))

    class Meta:
        model = ffInfo
        exclude=[]
  

#===========Man made feature========
class ManmadeFeatureForm(forms.ModelForm):
    featureID = forms.CharField(max_length=20, label="Manmade Feature ID", widget=forms.TextInput(attrs={'class':'form-control'}))
    watershedID = forms.ModelChoiceField(label='Relation to Watershed', queryset=Watershed.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=20, label="Name:", widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=255, label="Description:", widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))
    latitude = forms.CharField(max_length=20, label="Latitude:", widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitude = forms.CharField(max_length=20, label="Longitude:", widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = ManmadeFeature
        exclude=[]


#===========Natural feature ========
class NaturalFeatureForm(forms.ModelForm):
    featureID = forms.CharField(max_length=20, label="Natural Feature ID:", widget=forms.TextInput(attrs={'class':'form-control'}))
    watershedID = forms.ModelChoiceField(label='Relation to Watershed', queryset=Watershed.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    name = forms.CharField(max_length=20, label="Name:", widget=forms.TextInput(attrs={'class':'form-control'}))
    description = forms.CharField(max_length=255, label="Description:", widget=forms.Textarea(attrs={'class':'form-control', 'rows':'3'}))
    latitude = forms.CharField(max_length=20, label="Latitude:", widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitude = forms.CharField(max_length=20, label="Longitude:", widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = NaturalFeature
        exclude = []

#=========Observation ==============
class ObservationForm(forms.ModelForm):
    observationID = forms.CharField(max_length=20, label="ID:", widget=forms.TextInput(attrs={'class':'form-control'}))
    watershedID = forms.ModelChoiceField(label='Relation to Watershed', queryset=Watershed.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    date = forms.CharField(max_length=20, label="Date:", widget=forms.TextInput(attrs={'class':'form-control'}))
    testType = forms.CharField(max_length=20, label="Test Type:", widget=forms.TextInput(attrs={'class':'form-control'}))
    testLevel = forms.CharField(max_length=20, label="Test Level:", widget=forms.TextInput(attrs={'class':'form-control'}))
    latitude = forms.CharField(max_length=20, label="What is its latitude",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    longitude = forms.CharField(max_length=20, label="What is its longitude?",
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Observation
        exclude=[]

#=========WatershedPipe ==============
class WatershedPipeForm(forms.ModelForm):
    connectionID = forms.CharField(max_length=20, label="ID:", widget=forms.TextInput(attrs={'class':'form-control'}))
    # watershedID = forms.CharField(max_length=20, label="Relation to Watershed", widget=forms.TextInput(attrs={'class':'form-control'}))
    # pipeID = forms.CharField(max_length=20, label="Relation to Pipe", widget=forms.TextInput(attrs={'class':'form-control'}))
    # watershedID = forms.ModelChoiceField(label='Relation to Watershed', queryset=Watershed.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    # pipeID = forms.ModelChoiceField(label='Relation to Pipe', queryset=Pipe.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    watershedID = forms.ChoiceField(choices=(Watershed.objects.values_list('watershedID','name')),label='Relation to Watershed')
    pipeID = forms.ChoiceField(choices=(Pipe.objects.values_list('pipeid','pipeid')), label='Relation to Pipe')

    class Meta:
        model = WatershedPipe
        exclude=[]
