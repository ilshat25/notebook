from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from django.contrib.postgres.search import SearchVector

from .forms import EntryForm
from .models import EntryModel

# Create your views here.

@login_required
def index_view(request):
    entries = EntryModel.objects.filter(owner=request.user)
    return render(request, 'entries/index.html', {'entries': entries})

@login_required
def create_view(request):
    if request.method == 'POST':
        entry_form = EntryForm(request.POST, request.FILES)
        if entry_form.is_valid():
            entry = entry_form.save(commit=False)
            entry.owner = request.user
            entry.save()
            return redirect('index')
    else:
        entry_form = EntryForm()
    return render(request, 'entries/create.html', {'entry_form': entry_form})

@login_required
def change_view(request, pk):
    entry = get_object_or_404(EntryModel, pk=pk)
    if request.method == 'POST':
        entry_form = EntryForm(request.POST, request.FILES, instance=entry)
        if entry_form.is_valid():
            entry_form.save()
            return redirect('index')
    else:
        entry_form = EntryForm(instance=entry)
    return render(request, 'entries/create.html', {'entry_form': entry_form,
                                                   'entry': entry})

@login_required
def delete_view(request, pk):
    entry = get_object_or_404(EntryModel, pk=pk)
    entry.delete()
    return redirect('index')

@login_required
@require_GET
def search_view(request):
    query = request.GET.get('query', '')
    if query:
        entries = EntryModel.objects.annotate(
                        search=SearchVector('name', 'phone_number', 'address', 'comment')
                ).filter(search=query).all()
    else:
        return redirect('index')
    return render(request, 'entries/index.html', {'entries': entries})

