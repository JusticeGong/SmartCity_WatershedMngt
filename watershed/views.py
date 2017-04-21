from django.http import HttpResponse, Http404
from watershed.models import Watershed, FloraFauna
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


# ========== Forms =========

class WatershedCreateForm(ModelForm):
    class Meta:
     model = Watershed
     fields = ['watershedID', 'name', 'isProtected', 'percentLand', 'supportsTourism', 'watershedDescription', 'location']

class WatershedUpdateForm(ModelForm):
    class Meta:
        model = Watershed
        fields = ['name', 'isProtected', 'percentLand', 'supportsTourism', 'watershedDescription', 'location']

class FloraFaunaCreateForm(ModelForm):
    class Meta:
        model = FloraFauna
        fields = ['florafaunaID', 'name', 'species']

class FloraFaunaUpdateForm(ModelForm):
    class Meta:
        model = FloraFauna
        fields = ['name', 'species']

# ========== Home =========

def index(request):
    all_watershed = Watershed.objects.all()
    all_florafauna = FloraFauna.objects.all()
    context = {
        'all_watershed': all_watershed,
        'all_florafauna': all_florafauna
    }
    return render(request, 'watershed/index.html', context)

def detail(request, pk):
        watershed = get_object_or_404(Watershed, pk=pk)
        context = {
            'watershed': watershed
        }
        return render(request, 'watershed/detail.html', context)


def detail_florafauna(request, pk):
    florafauna = get_object_or_404(FloraFauna, pk=pk)
    context = {
        'florafauna': florafauna
    }
    return render(request, 'watershed/detail_florafauna.html', context)


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

def florafauna_view(request, pk, template_name='watershed/detail_florafauna.html'):
    flora= get_object_or_404(FloraFauna, pk=pk)
    ctx = {}
    ctx["flora"] = flora
    return render(request, template_name, ctx)

def florafauna_create(request, template_name='watershed/florafauna_form.html'):
    form = FloraFaunaCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def florafauna_update(request, pk, template_name='watershed/florafauna_update.html'):
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


def florafauna_delete(request, pk, template_name='watershed/florafauna_confirm_delete.html'):
    FloraFauna.objects.filter(florafaunaID=pk).delete()
    return redirect('watershed:index')
    ctx = {}
    ctx["object"] = flora
    ctx["flora"] = flora
    return render(request, template_name, ctx)