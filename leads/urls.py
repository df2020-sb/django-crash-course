from django.urls import path

from . import views

app_name = 'leads'

urlpatterns = [
    path('', views.lead_list),
    path('<int:id>/', views.lead_detail),
    path('create/', views.lead_create)
]