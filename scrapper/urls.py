from django.urls import path
from . import views
from downloader import views as download_views

urlpatterns = [
        path('',views.home,name='home'),
        path('download/',download_views.home,name='download-home'),
        path('downloading/',download_views.downloading,name='downloading')
    ]