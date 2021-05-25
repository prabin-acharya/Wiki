from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import random

from . import util


def index(request):
    entry_list = util.list_entries()
    if request.method == "POST":
        search = request.POST.get("search")

        if search is not None:
            search = search.lower().strip()
            for entry in entry_list:
                if search == entry.lower():
                    return redirect('titlepageview', title=entry)

            entry_list = list(filter(lambda x: search in x.lower(), entry_list))
            if not entry_list:
                return redirect(notFound)


    context = {"entries": util.list_entries()}
    return render(request, "encyclopedia/index.html", context)


def titlepage_view(request, title):
    entry_list = util.list_entries()
    if title is not None :
        title = title.lower().strip()
        for entry in entry_list:
            if title == entry.lower():
                context = {"title" : entry, "getentry": util.get_entry(entry)}
                return render(request, "encyclopedia/titlepage.html", context)


    
    context = {"title" : title}
    return render(request, "encyclopedia/entrynotfound.html", context)

def notFound(request):
    return render(request, "encyclopedia/entrynotfound.html")


def addentry_view(request):
    context = {}
    return render(request, "encyclopedia/addentry.html", context)

def edit_entry(request, title):
    content = util.get_entry(title)
    context = {"title": title , "content": content}
    return render(request, "encyclopedia/editentry.html", context)

def random_entry(request):
    entry_list=util.list_entries()
    if entry_list:
        title = random.choice(entry_list)
        return HttpResponseRedirect(reverse("titlepageview", args=(title,)))