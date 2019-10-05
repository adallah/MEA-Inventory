from django.urls import path, include
from . import views


urlpatterns = [
    path('portal/',views.store.as_view(),name='portal'),
    path('hardware/',views.hardware.as_view(),name='hardware'),
]