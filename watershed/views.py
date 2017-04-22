from django.http import HttpResponse, Http404
from watershed.models import *
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from watershed.forms import *



# ======== Generic CRUD ======

#CREATE
def generic_create(request, type):
    #Identify the type of form
    if type == 'Watershed':
        form = WatershedForm(request.POST or None)
    elif type == 'floraFauna':
        form = FloraFaunaForm(request.POST or None)
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
    else:
        form = None

    #Load form
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    ctx["type"] = type
    template_name='watershed/generic_form.html'
    return render(request, template_name, ctx)

#UPDATE
def generic_update(request, pk, type):
    #Identify the type of form
    if type == 'Watershed':
        watershed = get_object_or_404(Watershed, pk=pk)
        form = WatershedForm(request.POST or None, instance=watershed)
        form.fields['watershedID'].widget.attrs['readonly'] = True

    elif type == 'floraFauna':
        flora = get_object_or_404(FloraFauna, pk=pk)
        form = FloraFaunaForm(request.POST or None, instance=flora)

    elif type == 'Maintenance':
        maintenance = get_object_or_404(Maintenance, pk=pk)
        form=MaintenanceForm(request.POST or None, instance=maintenance)

    elif type == 'Observation':
        observation = get_object_or_404(Observation, pk=pk)
        form = ObservationForm(request.POST or None, instance=observation)

    elif type == 'Natural Feature':
        naturalFeature = get_object_or_404(NaturalFeature, pk=pk)
        form = NaturalFeatureForm(request.POST or None, instance=naturalFeature)

    elif type == 'Manmade Feature':
        manMadeFeature = get_object_or_404(ManmadeFeature, pk=pk)
        form = ManmadeFeatureForm(request.POST or None, instance=manMadeFeature)

    elif type == 'ffinfo':
        ffInfoInstance=get_object_or_404(ffInfo, pk=pk)
        form = ffInfoForm(request.POST or None, instance=ffInfoInstance)
    else:
        form = None

    #Load form
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    ctx['type'] = type
    template_name='watershed/generic_form.html'
    return render(request, template_name, ctx)

#READ
def generic_detail(request, pk, type):
    ctx={}
    ctx['type']=type
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


        ctx['watershed']=watershed
        ctx['maintenance']=maintenance
        ctx['manMadeFeatures']=manMadeFeatures
        ctx['naturalFeatures']=naturalFeatures
        ctx['observationV']=observationV
        ctx['FloraAndFauna']=FloraAndFauna
        template_name='watershed/detail.html'

    elif type == 'floraFauna':
        florafauna = get_object_or_404(FloraFauna, pk=pk)
        ctx['entity']=florafauna

    elif type == 'Maintenance':
        maintenance = get_object_or_404(Maintenance, pk=pk)
        ctx['entity']=maintenance

    elif type == 'Observation':
        obs=get_object_or_404(Observation, pk=pk)
        ctx['entity']=obs

    elif type == 'Natural Feature':
        natF=get_object_or_404(NaturalFeature, pk=pk)
        ctx['entity']=natF

    elif type == 'Manmade Feature':
        manmade=get_object_or_404(ManmadeFeature, pk=pk)
        ctx['entity']=manmade

    elif type == 'ffinfo':
        ffInfoV=get_object_or_404(ffInfo, pk=pk)
        ctx['entity']=ffInfoV

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
    context = {
        'all_watershed': all_watershed,
        'all_florafauna': all_florafauna,
        'all_maintenance': all_maintenance,
        'all_manmadefeature': all_manmadefeature,
        'all_naturalfeature': all_naturalfeature,
        'all_ffinfo': all_ffinfo,
        'all_observation': all_observation
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




