from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()

    })


def EntryPage(request, title):
    #if request.method == "POST":
    #    title = request.POST    

    return render(request, "encyclopedia/entrypage.html", {
        "title" : title,
        "getentry": util.get_entry(title)
        })

