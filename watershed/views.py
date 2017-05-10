from django.http import HttpResponse, Http404
from watershed.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from watershed.forms import *
from django.http import Http404


# #Generate GeoRSS
# def GeoRSS

def twentymindrive_map(request, type):
    template_name = 'watershed/twentymindrive_map.html'
    return render(request, template_name)

def waterlevel_map(request, type):
    template_name = 'watershed/waterlevel_map.html'
    return render(request, template_name)

def GenerateGeoRSS(request, type):
    # GeoRssGenerator()
    #Load form
    template_name='watershed/index.html'
    return index(request)



# ======== Generic CRUD ======

#CREATE
def generic_create(request, type):
    #Identify the type of form
    ctx={}
    ctx["type"] = type

    if type == 'Watershed':
        form = WatershedForm(request.POST or None)
    elif type == 'floraFauna':
        form = FloraFaunaForm(request.POST or None)
        ctx['type'] = 'Flora and Fauna'
    elif type == 'Maintenance':
        form = MaintenanceForm(request.POST or None)
    elif type == 'Observation':
        form = ObservationForm(request.POST or None)
    elif type == 'Natural Feature':
        form = NaturalFeatureForm(request.POST or None)
    elif type == 'Manmade Feature':
        form = ManmadeFeatureForm(request.POST or None)
    elif type == 'ffinfo':
        form = ffInfoForm(request.POST or None)
        ctx['type'] = 'Flora and Fauna Specifics'
    elif type == 'WatershedPipeConnection':
        form = WatershedPipeForm(request.POST or None)
        ctx['type']='Watershed - Pipe Connection'

    else:
        form = None

    #Load form
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx["form"] = form
  
    template_name='watershed/generic_form.html'
    return render(request, template_name, ctx)

#UPDATE
def generic_update(request, pk, type):
    #Identify the type of form
    ctx = {}
    if type == 'Watershed':
        watershed = get_object_or_404(Watershed, pk=pk)
        form = WatershedForm(request.POST or None, instance=watershed)
        form.fields['watershedID'].widget.attrs['readonly'] = True

    elif type == 'floraFauna':
        flora = get_object_or_404(FloraFauna, pk=pk)
        form = FloraFaunaForm(request.POST or None, instance=flora)
        ctx['type'] = 'Flora and Fauna'
        form.fields['florafaunaID'].widget.attrs['readonly'] = True

    elif type == 'Maintenance':
        maintenance = get_object_or_404(Maintenance, pk=pk)
        form=MaintenanceForm(request.POST or None, instance=maintenance)
        form.fields['watershedID'].widget.attrs['readonly'] = True
        form.fields['maintenanceID'].widget.attrs['readonly'] = True

    elif type == 'Observation':
        observation = get_object_or_404(Observation, pk=pk)
        form = ObservationForm(request.POST or None, instance=observation)
        form.fields['watershedID'].widget.attrs['readonly'] = True
        form.fields['observationID'].widget.attrs['readonly'] = True

    elif type == 'Natural Feature':
        naturalFeature = get_object_or_404(NaturalFeature, pk=pk)
        form = NaturalFeatureForm(request.POST or None, instance=naturalFeature)
        form.fields['watershedID'].widget.attrs['readonly'] = True
        form.fields['featureID'].widget.attrs['readonly'] = True


    elif type == 'Manmade Feature':
        manMadeFeature = get_object_or_404(ManmadeFeature, pk=pk)
        form = ManmadeFeatureForm(request.POST or None, instance=manMadeFeature)
        form.fields['watershedID'].widget.attrs['readonly'] = True
        form.fields['featureID'].widget.attrs['readonly'] = True

    elif type == 'ffinfo':
        ffInfoInstance=get_object_or_404(ffInfo, pk=pk)
        form = ffInfoForm(request.POST or None, instance=ffInfoInstance)
        ctx['type'] = 'Flora and Fauna Specifics'
        form.fields['watershedID'].widget.attrs['readonly'] = True
        form.fields['florafaunaID'].widget.attrs['readonly'] = True
        form.fields['ffInfoID'].widget.attrs['readonly'] = True

    elif type == 'WatershedPipeConnection':
        wpconnection =get_object_or_404(WatershedPipe, pk=pk)
        form = WatershedPipeForm(request.POST or None, instance= wpconnection)
        ctx['type']='Watershed - Pipe Connection'

    else:
        form = None

    #Load form
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    
    ctx["form"] = form
    ctx['type'] = type
    template_name='watershed/generic_form.html'
    return render(request, template_name, ctx)

#READ
def generic_detail(request, pk, type):
    ctx={}
    ctx['type']=type
    ctx['pk']=pk
    ctx['Add']=''
    ctx['Delete']=''
    ctx['update']=''
    template_name='watershed/generic_detail.html'

    if type == 'Watershed':
        watershed = get_object_or_404(Watershed, pk=pk)
        try:
            maintenance = Maintenance.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            maintenance = None
        try:
            manMadeFeatures = ManmadeFeature.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            manMadeFeatures = None
        try:
            naturalFeatures = NaturalFeature.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            naturalFeatures = None
        try:
            observationV = Observation.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            observationV = None
        try:
            FloraAndFauna = ffInfo.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            FloraAndFauna = None
        try:
            WPConnection = WatershedPipe.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            WPConnection = None

        ctx['watershed']=watershed
        ctx['maintenance']=maintenance
        ctx['manMadeFeatures']=manMadeFeatures
        ctx['naturalFeatures']=naturalFeatures
        ctx['observationV']=observationV
        ctx['FloraAndFauna']=FloraAndFauna
        ctx['WPConnection'] = WPConnection
        template_name='watershed/detail.html'

    elif type == 'floraFauna':
        florafauna = get_object_or_404(FloraFauna, pk=pk)
        ctx['entity']=florafauna
        ctx['Add']='watershed:florafauna_new'
        ctx['Delete']='watershed:florafauna_delete'
        ctx['Update']='watershed:florafauna_update'
        ctx['type'] = 'Flora and Fauna'

    elif type == 'Maintenance':
        maintenance = get_object_or_404(Maintenance, pk=pk)
        ctx['entity']=maintenance
        ctx['Add']='watershed:maintenance_new'
        ctx['Delete']='watershed:maintenance_delete'
        ctx['Update']='watershed:maintenance_update'

    elif type == 'Observation':
        obs=get_object_or_404(Observation, pk=pk)
        ctx['entity']=obs
        ctx['Add']='watershed:observation_new'
        ctx['Delete']='watershed:observation_delete'
        ctx['Update']='watershed:observation_update'

    elif type == 'Natural Feature':
        natF=get_object_or_404(NaturalFeature, pk=pk)
        ctx['entity']=natF
        ctx['Add']='watershed:naturalfeature_new'
        ctx['Delete']='watershed:naturalfeature_delete'
        ctx['Update']='watershed:naturalfeature_update'


    elif type == 'Manmade Feature':
        manmade=get_object_or_404(ManmadeFeature, pk=pk)
        ctx['entity']=manmade
        ctx['Add']='watershed:manmadefeature_new'
        ctx['Delete']='watershed:manmadefeature_delete'
        ctx['Update']='watershed:manmadefeature_update'

    elif type == 'ffinfo':
        ffInfoV=get_object_or_404(ffInfo, pk=pk)
        ctx['entity']=ffInfoV
        ctx['Add']='watershed:ffinfo_new'
        ctx['Delete']='watershed:ffinfo_delete'
        ctx['Update']='watershed:ffinfo_update'
        ctx['type'] = 'Flora and Fauna Specifics'

    elif type == 'WatershedPipeConnection':
        wpc=get_object_or_404(WatershedPipe, pk=pk)
        ctx['entity']=wpc
        ctx['Add']='watershed:wpconnection_new'
        ctx['Delete']='watershed:wpconnection_delete'
        ctx['Update']='watershed:wpconnection_update'
        ctx['type']='Watershed - Pipe Connection'

    else:
        form = None

    #Load form
    return render(request, template_name, ctx)

#DELETE
def generic_delete(request, pk, type):
    if type == 'Watershed':
        Watershed.objects.filter(watershedID=pk).delete()
    elif type == 'floraFauna':
        FloraFauna.objects.filter(florafaunaID=pk).delete()
    elif type == 'Maintenance':
        Maintenance.objects.filter(maintenanceID=pk).delete()
    elif type == 'Observation':
        Observation.objects.filter(observationID=pk).delete()
    elif type == 'Natural Feature':
        NaturalFeature.objects.filter(featureID=pk).delete()
    elif type == 'Manmade Feature':
        ManmadeFeature.objects.filter(featureID=pk).delete()
    elif type == 'ffinfo':
        ffInfo.objects.filter(ffInfoID=pk).delete()
    elif type == 'WatershedPipeConnection':
        WatershedPipe.objects.filter(connectionID=pk).delete()
    else:
        pass

    #Load form
    template_name='watershed/index.html'
    return index(request) 



# ========== Home =========

def index(request):



    all_watershed = Watershed.objects.all()
    all_florafauna = FloraFauna.objects.all()
    all_maintenance = Maintenance.objects.all()
    all_manmadefeature = ManmadeFeature.objects.all()
    all_naturalfeature = NaturalFeature.objects.all()
    all_ffinfo = ffInfo.objects.all()
    all_observation = Observation.objects.all()
    all_watershedpipe = WatershedPipe.objects.all()

    context = {
        'all_watershed': all_watershed,
        'all_florafauna': all_florafauna,
        'all_maintenance': all_maintenance,
        'all_manmadefeature': all_manmadefeature,
        'all_naturalfeature': all_naturalfeature,
        'all_ffinfo': all_ffinfo,
        'all_observation': all_observation,
        'all_watershedpipe': all_watershedpipe,
    }
    return render(request, 'watershed/index.html', context)



# def watershed_delete(request, pk, template_name='watershed/watershed_confirm_delete.html'):
#     Watershed.objects.filter(watershedID=pk).delete()
#     return redirect('watershed:index')
#     ctx = {}
#     ctx["object"] = watershed
#     ctx["watershed"] = watershed
#     return render(request, template_name, ctx)

# def florafauna_delete(request, pk, template_name='watershed/florafauna/watershed_confirm_delete.html'):
#     FloraFauna.objects.filter(florafaunaID=pk).delete()
#     return redirect('watershed:index')
#     ctx = {}
#     ctx["object"] = flora
#     ctx["flora"] = flora
#     return render(request, template_name, ctx)

# def maintenance_delete(request, pk, template_name='watershed/maintenance/watershed_confirm_delete.html'):
#     Maintenance.objects.filter(maintenanceID=pk).delete()
#     return redirect('watershed:index')
#     ctx = {}
#     ctx["object"] = maintenance
#     ctx["maintenance"] = maintenance
#     return render(request, template_name, ctx)




