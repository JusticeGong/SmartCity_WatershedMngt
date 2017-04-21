from django.http import HttpResponse, Http404
from watershed.models import Watershed, FloraFauna, Maintenance, ManmadeFeature, NaturalFeature, ffInfo, Observation
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist


# ========== Watershed Forms =========

class WatershedCreateForm(ModelForm):
    class Meta:
     model = Watershed
     fields = ['watershedID', 'name', 'isProtected', 'percentLand', 'supportsTourism', 'watershedDescription', 'location']

class WatershedUpdateForm(ModelForm):
    class Meta:
        model = Watershed
        fields = ['name', 'isProtected', 'percentLand', 'supportsTourism', 'watershedDescription', 'location']

# ========== FloraFauna Forms =========

class FloraFaunaCreateForm(ModelForm):
    class Meta:
        model = FloraFauna
        fields = ['florafaunaID', 'name', 'species']

class FloraFaunaUpdateForm(ModelForm):
    class Meta:
        model = FloraFauna
        fields = ['name', 'species']

# ========== Maintenance Forms =========

class MaintenanceCreateForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ['watershedID', 'maintenanceID', 'date','issue','cost','locationofElement', 'status']

class MaintenanceUpdateForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = ['date','issue','cost','locationofElement', 'status']

# ========== Maintenance Forms =========

class ManmadeFeatureCreateForm(ModelForm):
    class Meta:
        model = ManmadeFeature
        fields = ['watershedID', 'featureID', 'name', 'description']

class ManmadeFeatureUpdateForm(ModelForm):
    class Meta:
        model = ManmadeFeature
        fields = ['name', 'description']

# ========== Maintenance Forms =========

class NaturalFeatureCreateForm(ModelForm):
    class Meta:
        model = NaturalFeature
        fields = ['watershedID', 'featureID', 'name', 'description']

class NaturalFeatureUpdateForm(ModelForm):
    class Meta:
        model = NaturalFeature
        fields = ['name', 'description']

# ========== Maintenance Forms =========

class ffInfoCreateForm(ModelForm):
    class Meta:
        model = ffInfo
        fields = ['watershedID', 'florafaunaID', 'ffInfoID', 'isNative', 'description', 'photoUrl']

class ffInfoUpdateForm(ModelForm):
    class Meta:
        model = ffInfo
        fields = ['isNative', 'description', 'photoUrl']

# ========== Maintenance Forms =========

class ObservationCreateForm(ModelForm):
    class Meta:
        model = Observation
        fields = ['watershedID', 'observationID', 'sublocation', 'date', 'description', 'testType']

class ObservationUpdateForm(ModelForm):
    class Meta:
        model = Observation
        fields = ['sublocation', 'date', 'description', 'testType']

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
        'all_observation': all_observation,
    }
    return render(request, 'watershed/index.html', context)

# ========== Watershed complete detail page =========

def detail(request, pk):
        watershed = get_object_or_404(Watershed, pk=pk)
        #maintenance = Maintenance.objects.filter(watershedID=pk).get()
        print(watershed)
        try:
            maintenance = Maintenance.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            maintenance = None
        print (maintenance)
        try:
            manmadefeature = ManmadeFeature.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            manmadefeature = None
        print (manmadefeature)
        try:
            naturalfeature = NaturalFeature.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            naturalfeature = None
        print (naturalfeature)
        try:
            ffinfo = ffInfo.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            ffinfo = None
        print (ffinfo)
        try:
            observation = Observation.objects.all().filter(watershedID=pk)
        except ObjectDoesNotExist:
            observation = None
        print (observation)
        context = {
            'watershed': watershed,
            'maintenance': maintenance,
            'manmadefeature': manmadefeature,
            'naturalfeature': naturalfeature,
            'ffinfo': ffinfo,
            'observation': observation
        }
        return render(request, 'watershed/detail.html', context)

# ========== FloraFauna detail page =========

def detail_florafauna(request, pk):
    florafauna = get_object_or_404(FloraFauna, pk=pk)
    context = {
        'florafauna': florafauna
    }
    return render(request, 'watershed/florafauna/detail_florafauna.html', context)

# ========== Maintenance detail page =========

def detail_maintenance(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)
    context = {
        'maintenance': maintenance
    }
    return render(request, 'watershed/maintenance/detail_maintenance.html', context)

# ========== ManmadeFeature detail page =========

def detail_manmadefeature(request, pk):
    manmadefeature = get_object_or_404(ManmadeFeature, pk=pk)
    context = {
        'manmadefeature': manmadefeature
    }
    return render(request, 'watershed/manmadefeature/detail_manmadefeature.html', context)

# ========== NaturalFeature detail page =========

def detail_naturalfeature(request, pk):
    naturalfeature = get_object_or_404(NaturalFeature, pk=pk)
    context = {
        'naturalfeature': naturalfeature
    }
    return render(request, 'watershed/naturalfeature/detail_naturalfeature.html', context)

# ========== ffInfo detail page =========

def detail_ffinfo(request, pk):
    ffinfo = get_object_or_404(ffInfo, pk=pk)
    context = {
        'ffinfo': ffinfo
    }
    return render(request, 'watershed/ffinfo/detail_ffinfo.html', context)

# ========== Observation detail page =========

def detail_observation(request, pk):
    observation = get_object_or_404(Observation, pk=pk)
    context = {
        'observation': observation
    }
    return render(request, 'watershed/observation/detail_observation.html', context)

# ========== Watershed CRUD =========

def watershed_view(request, watershed_id, template_name='watershed/detail.html'):
    watershed= get_object_or_404(Watershed, pk=watershed_id)
    ctx = {}
    ctx["watershed"] = watershed
    return render(request, template_name, ctx)

def watershed_create(request, template_name='watershed/watershed_form.html'):
    form = WatershedCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def watershed_update(request, pk, template_name='watershed/watershed_update.html'):
    watershed = get_object_or_404(Watershed, pk=pk)
    form = WatershedUpdateForm(request.POST or None, instance=watershed)

    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    # Watershed.objects.filter(watershedID=pk).delete()
    ctx = {}
    ctx["form"] = form
    ctx["watershed"] = watershed
    return render(request, template_name, ctx)


def watershed_delete(request, pk, template_name='watershed/watershed_confirm_delete.html'):
    Watershed.objects.filter(watershedID=pk).delete()
    return redirect('watershed:index')
    ctx = {}
    ctx["object"] = watershed
    ctx["watershed"] = watershed
    return render(request, template_name, ctx)


# ========== FloraFauna CRUD =========

def florafauna_view(request, pk, template_name='watershed/florafauna/detail_florafauna.html'):
    flora= get_object_or_404(FloraFauna, pk=pk)
    ctx = {}
    ctx["flora"] = flora
    return render(request, template_name, ctx)

def florafauna_create(request, template_name='watershed/florafauna/florafauna_form.html'):
    form = FloraFaunaCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def florafauna_update(request, pk, template_name='watershed/florafauna/florafauna_update.html'):
    flora = get_object_or_404(FloraFauna, pk=pk)
    form = FloraFaunaUpdateForm(request.POST or None, instance=flora)

    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    # Watershed.objects.filter(watershedID=pk).delete()
    ctx = {}
    ctx["form"] = form
    ctx["flora"] = flora
    return render(request, template_name, ctx)


def florafauna_delete(request, pk, template_name='watershed/florafauna/florafauna_confirm_delete.html'):
    FloraFauna.objects.filter(florafaunaID=pk).delete()
    return redirect('watershed:index')
    ctx = {}
    ctx["object"] = flora
    ctx["flora"] = flora
    return render(request, template_name, ctx)

# ========== Maintenance CRUD =========

def maintenance_view(request, maintenance_id, template_name='watershed/maintenance/detail_maintenance.html'):
    maintenance= get_object_or_404(Maintenance, pk=maintenance_id)
    ctx = {}
    ctx["maintenance"] = maintenance
    return render(request, template_name, ctx)

def maintenance_create(request, template_name='watershed/maintenance/maintenance_form.html'):
    form = MaintenanceCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def maintenance_update(request, pk, template_name='watershed/maintenance/maintenance_update.html'):
    maintenance = get_object_or_404(Maintenance, pk=pk)
    form = MaintenanceUpdateForm(request.POST or None, instance=maintenance)

    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    # Watershed.objects.filter(watershedID=pk).delete()
    ctx = {}
    ctx["form"] = form
    ctx["maintenance"] = maintenance
    return render(request, template_name, ctx)


def maintenance_delete(request, pk, template_name='watershed/maintenance/maintenance_confirm_delete.html'):
    Maintenance.objects.filter(maintenanceID=pk).delete()
    return redirect('watershed:index')
    ctx = {}
    ctx["object"] = maintenance
    ctx["maintenance"] = maintenance
    return render(request, template_name, ctx)

# ========== ManmadeFeature CRUD =========

def manmadefeature_view(request, manmadefeature_id, template_name='watershed/manmadefeature/detail_manmadefeature.html'):
    manmadefeature= get_object_or_404(ManmadeFeature, pk=manmadefeature_id)
    ctx = {}
    ctx["manmadefeature"] = manmadefeature
    return render(request, template_name, ctx)

def manmadefeature_create(request, template_name='watershed/manmadefeature/manmadefeature_form.html'):
    form = ManmadeFeatureCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def manmadefeature_update(request, pk, template_name='watershed/manmadefeature/manmadefeature_update.html'):
    manmadefeature = get_object_or_404(ManmadeFeature, pk=pk)
    form = ManmadeFeatureUpdateForm(request.POST or None, instance=manmadefeature)

    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    # Watershed.objects.filter(watershedID=pk).delete()
    ctx = {}
    ctx["form"] = form
    ctx["manmadefeature"] = manmadefeature
    return render(request, template_name, ctx)


def manmadefeature_delete(request, pk, template_name='watershed/manmadefeature/manmadefeature_confirm_delete.html'):
    ManmadeFeature.objects.filter(featureID=pk).delete()
    return redirect('watershed:index')
    ctx = {}
    ctx["object"] = manmadefeature
    ctx["manmadefeature"] = manmadefeature
    return render(request, template_name, ctx)

# ========== NaturalFeature CRUD =========

def naturalfeature_view(request, naturalfeature_id, template_name='watershed/naturalfeature/detail_naturalfeature.html'):
    naturalfeature= get_object_or_404(NaturalFeature, pk=naturalfeature_id)
    ctx = {}
    ctx["naturalfeature"] = naturalfeature
    return render(request, template_name, ctx)

def naturalfeature_create(request, template_name='watershed/naturalfeature/naturalfeature_form.html'):
    form = NaturalFeatureCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def naturalfeature_update(request, pk, template_name='watershed/naturalfeature/naturalfeature_update.html'):
    naturalfeature = get_object_or_404(NaturalFeature, pk=pk)
    form = NaturalFeatureUpdateForm(request.POST or None, instance=naturalfeature)

    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    # Watershed.objects.filter(watershedID=pk).delete()
    ctx = {}
    ctx["form"] = form
    ctx["naturalfeature"] = naturalfeature
    return render(request, template_name, ctx)


def naturalfeature_delete(request, pk, template_name='watershed/naturalfeature/naturalfeature_confirm_delete.html'):
    NaturalFeature.objects.filter(featureID=pk).delete()
    return redirect('watershed:index')
    ctx = {}
    ctx["object"] = naturalfeature
    ctx["naturalfeature"] = naturalfeature
    return render(request, template_name, ctx)

# ========== ffInfo CRUD =========

def ffinfo_view(request, ffinfo_id, template_name='watershed/ffinfo/detail_ffinfo.html'):
    ffinfo= get_object_or_404(ffInfo, pk=ffinfo_id)
    ctx = {}
    ctx["ffinfo"] = ffinfo
    return render(request, template_name, ctx)

def ffinfo_create(request, template_name='watershed/ffinfo/ffinfo_form.html'):
    form = ffInfoCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def ffinfo_update(request, pk, template_name='watershed/ffinfo/ffinfo_update.html'):
    ffinfo = get_object_or_404(ffInfo, pk=pk)
    form = ffInfoUpdateForm(request.POST or None, instance=ffinfo)

    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    # Watershed.objects.filter(watershedID=pk).delete()
    ctx = {}
    ctx["form"] = form
    ctx["ffinfo"] = ffinfo
    return render(request, template_name, ctx)


def ffinfo_delete(request, pk, template_name='watershed/ffinfo/ffinfo_confirm_delete.html'):
    ffInfo.objects.filter(ffInfoID=pk).delete()
    return redirect('watershed:index')
    ctx = {}
    ctx["object"] = ffinfo
    ctx["ffinfo"] = ffinfo
    return render(request, template_name, ctx)

# ========== Observation CRUD =========

def observation_view(request, observation_id, template_name='watershed/observation/detail_observation.html'):
    observation= get_object_or_404(Observation, pk=observation_id)
    ctx = {}
    ctx["observation"] = observation
    return render(request, template_name, ctx)

def observation_create(request, template_name='watershed/observation/observation_form.html'):
    form = ObservationCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def observation_update(request, pk, template_name='watershed/observation/observation_update.html'):
    observation = get_object_or_404(Observation, pk=pk)
    form = ObservationUpdateForm(request.POST or None, instance=observation)

    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    # Watershed.objects.filter(watershedID=pk).delete()
    ctx = {}
    ctx["form"] = form
    ctx["observation"] = observation
    return render(request, template_name, ctx)


def observation_delete(request, pk, template_name='watershed/observation/observation_confirm_delete.html'):
    Observation.objects.filter(observationID=pk).delete()
    return redirect('watershed:index')
    ctx = {}
    ctx["object"] = observation
    ctx["observation"] = observation
    return render(request, template_name, ctx)