from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('viewdata',views.viewdata, name='viewdata'),
    path('mat_analysis',views.mat_analysis, name='mat_analysis'),
    path('analysis',views.analysis, name='analysis'),
    path('materials',views.materials, name='materials'),
]