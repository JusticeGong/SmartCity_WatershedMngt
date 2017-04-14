from django.http import HttpResponse, Http404
from .models import Watershed,ffInfo,ManmadeFeature,NaturalFeature,Maintenance,FloraFauna,Observation
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

def index(request):
    all_watershed = Watershed.objects.all()
    context = {
        'all_watershed': all_watershed
    }
    return render(request, 'watershed/index.html', context)


def detail(request, watershed_id):
        watershed = get_object_or_404(Watershed, pk=watershed_id)
        context = {
            'watershed': watershed
        }
        return render(request, 'watershed/detail.html', context)


# ========== Forms =========

class WatershedForm(ModelForm):
    class Meta:
        model = Watershed
        fields = ['watershedID', 'name', 'percentLand', 'supportsTourism', 'watershedDescription', 'location']

# ========== Home =========

def home(request, template_name='watershed/index.html'):
    watersheds = Watershed.objects.all()
    ctx = {}
    ctx['watersheds'] = watersheds
    return render(request, template_name, ctx)


# ========== Watershed CRUD =========

def watershed_view(request, pk, template_name='watershed/watershed_view.html'):
    watershed = get_object_or_404(Watershed, pk=pk)
    ctx = {}
    ctx["watershed"] = watershed
    return render(request, template_name, ctx)


def watershed_create(request, template_name='watershed/watershed_form.html'):
    form = WatershedForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:home')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def watershed_update(request, pk, template_name='watershed/watershed_form.html'):
    watershed = get_object_or_404(Watershed, pk=pk)
    form = WatershedForm(request.POST or None, instance=watershed)
    if form.is_valid():
        form.save()
        return redirect('watershed:home')
    ctx = {}
    ctx["form"] = form
    ctx["watershed"] = watershed
    return render(request, template_name, ctx)


def watershed_delete(request, pk, template_name='watershed/watershed_confirm_delete.html'):
    watershed = get_object_or_404(Watershed, pk=pk)
    if request.method == 'POST':
        watershed.delete()
        return redirect('watershed:home')
    ctx = {}
    ctx["object"] = watershed
    ctx["watershed"] = watershed
    return render(request, template_name, ctx)
