from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.cooklist, name='list'),
    path('see/<int:Rid>', views.see, name='see'),
    path('add/', views.add, name='add'),
]
