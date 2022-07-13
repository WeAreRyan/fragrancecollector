from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name="about"), 
    path('fragrances/', views.fragrances_index, name='index'), 
    path('fragrances/<int:fragrance_id>/', views.fragrances_detail, name='detail'), 
    path('fragrances/create', views.FragranceCreate.as_view(), name='fragrances_create'), 
    path('fragrances/<int:pk>/update', views.FragranceUpdate.as_view(), name='fragrances_update'), 
    path('fragrances/<int:pk>/delete/', views.FragranceDelete.as_view(), name='fragrances_delete'), 
    path('fragrances/<int:fragrance_id>/add_purchase/', views.add_purchase, name='add_purchase'),
]