from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Fragrance
from .forms import PurchaseForm

# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request): 
    return render(request, 'about.html')

def fragrances_index(request):
    fragrances = Fragrance.objects.all()
    return render(request, 'fragrances/index.html', { 'fragrances': fragrances })

def fragrances_detail(request, fragrance_id):
    fragrance = Fragrance.objects.get(id=fragrance_id)
    purchase_form = PurchaseForm()
    return render(request, 'fragrances/detail.html', {'fragrance': fragrance, 'purchase_form': purchase_form})

class FragranceCreate(CreateView):
  model = Fragrance 
  fields = '__all__'

class FragranceUpdate(UpdateView):
  model = Fragrance
  fields = ['name', 'brand', 'description', 'release_year']

class FragranceDelete(DeleteView):
  model = Fragrance
  success_url = '/fragrances/'

def add_purchase(request, fragrance_id):
    form = PurchaseForm(request.POST)
    if form.is_valid():
        new_purchase = form.save(commit=False)
        new_purchase.fragrance_id = fragrance_id
        new_purchase.save()
    return redirect('detail', fragrance_id=fragrance_id)
