from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/',views.makeBook),
    path('namebook/',views.allBooks),
    path('pubdate/',views.pubDate)
]