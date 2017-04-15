from django.http import HttpResponse, Http404
from watershed.models import Watershed
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm


# ========== Forms =========

class WatershedForm(ModelForm):
    class Meta:
     model = Watershed
     fields = ['name', 'percentLand', 'supportsTourism', 'watershedDescription', 'location']

# ========== Home =========

def index(request):
    all_watershed = Watershed.objects.all()
    context = {
        'all_watershed': all_watershed
    }
    return render(request, 'watershed/index.html', context)

def detail(request, pk):
        watershed = get_object_or_404(Watershed, pk=pk)
        context = {
            'watershed': watershed
        }
        return render(request, 'watershed/detail.html', context)


# ========== Watershed CRUD =========

def watershed_view(request, watershed_id, template_name='watershed/detail.html'):
    watershed= get_object_or_404(Watershed, pk=watershed_id)
    ctx = {}
    ctx["watershed"] = watershed
    return render(request, template_name, ctx)

def watershed_create(request, template_name='watershed/watershed_form.html'):
    form = WatershedForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('watershed:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def watershed_update(request, pk, template_name='watershed/watershed_update.html'):
    watershed = get_object_or_404(Watershed, pk=pk)
    form = WatershedForm(request.POST or None, instance=watershed)

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
    return render(request, template_name, ctx)

