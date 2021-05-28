from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("wiki/<str:title>/", views.wiki_entry, name="wikientry"),
    #re_path(r"^wiki/(?P<title>).*[\s\w]*/$", views.wiki_entry, name="wikientry"),
    path("wiki/entry-not-found/", views.notFound, name='entrynotfound'),
    path("add-entry/", views.add_entry, name='addentry'),
    path("random-entry/", views.random_entry, name='randomentry'),
    path("edit-entry/<str:title>/", views.edit_entry, name='editentry')
    ]


