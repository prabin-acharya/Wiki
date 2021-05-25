from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("wiki/<str:title>/", views.titlepage_view, name="titlepageview"),
    re_path(r"^wiki/(?P<title>).*[\s\w]*/$", views.titlepage_view, name="titlepageview"),
    path("wiki/entrynotfound/", views.notFound, name='entrynotfound'),
    path("addentry/", views.addentry_view, name='addentry'),
    path("random-entry/", views.random_entry, name='random_entry')
    ]


