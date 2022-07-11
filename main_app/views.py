from django.shortcuts import render
from django.http import HttpResponse


class Fragrance:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, brand, description, release_year):
    self.name = name
    self.brand = brand
    self.description = description
    self.release_year = release_year

fragrances = [
  Fragrance('Aventus', 'Creed', 'Aromatic Fougèr', 2010),
  Fragrance('Versace Pour Homme', 'Versace', 'Fresh Aquatic', 2008),
  Fragrance('Uomo Casual Life', 'Salvatore Ferragamo', 'Woody Aromatic', 2017)
]




# Create your views here.

def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request): 
    return render(request, 'about.html')

def fragrances_index(request):
    return render(request, 'fragrances/index.html', { 'fragrances': fragrances })