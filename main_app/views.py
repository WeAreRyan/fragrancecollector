from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Fragrance, Note
from .forms import PurchaseForm

# Create your views here.


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def fragrances_index(request):
    fragrances = Fragrance.objects.all()
    return render(request, "fragrances/index.html", {"fragrances": fragrances})


def fragrances_detail(request, fragrance_id):
    fragrance = Fragrance.objects.get(id=fragrance_id)
    id_list = fragrance.notes.all().values_list("id")
    np_notes = Note.objects.exclude(id__in=id_list)
    purchase_form = PurchaseForm()
    return render(
        request,
        "fragrances/detail.html",
        {"fragrance": fragrance, "purchase_form": purchase_form, 'notes': np_notes},
    )

def assoc_note(request, fragrance_id, note_id):
  Fragrance.objects.get(id=fragrance_id).notes.add(note_id)
  return redirect('detail', fragrance_id=fragrance_id)


class FragranceCreate(CreateView):
    model = Fragrance
    fields = ["name", "brand", "release_year"]


class FragranceUpdate(UpdateView):
    model = Fragrance
    fields = ["name", "brand", "description", "release_year"]


class FragranceDelete(DeleteView):
    model = Fragrance
    success_url = "/fragrances/"


def add_purchase(request, fragrance_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.fragrance_id = fragrance_id
        new_purchase.save()
    return redirect("detail", fragrance_id=fragrance_id)


class NoteList(ListView):
    model = Note


class NoteDetail(DetailView):
    model = Note


class NoteCreate(CreateView):
    model = Note
    fields = "__all__"


class NoteUpdate(UpdateView):
    model = Note
    fields = ["description", "category"]


class NoteDelete(DeleteView):
    model = Note
    success_url = "/notes/"
