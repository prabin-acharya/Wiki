from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
import random

from . import util


#Home page 
def index(request):
    entry_list = util.list_entries()
    if request.method == "POST": 
        search = request.POST.get("search")
        if search is not None:
            search = search.lower().strip()
            for entry in entry_list:
                if search == entry.lower():
                    return redirect(wiki_entry, title=entry)
                    #Here,if "wikientry" it will redirect to url with name wikientry but
                    #here it redirects to view function wiki_entry.

            entry_list = list(filter(lambda x: search in x.lower(), entry_list))
            if not entry_list:
                return redirect(notFound)

    context = {"entries": util.list_entries()}
    return render(request, "encyclopedia/index.html", context)


#Title page for an entry.
def wiki_entry(request, title):
    entry_list = util.list_entries()
    if title is not None :
        title = title.lower().strip()
        for entry in entry_list:
            if title == entry.lower():
                context = {"title" : entry, "getentry": util.get_entry(entry)}
                return render(request, "encyclopedia/wikientry.html", context)
    
    context = {"title" : title}
    return render(request, "encyclopedia/entrynotfound.html", context)


#Entry not found page.
def notFound(request):
    return render(request, "encyclopedia/entrynotfound.html")


#Add new entry to the encyclopedia. 
def add_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        entry_list = util.list_entries()
        for entry in entry_list:
            if title.lower().strip() == entry.lower():
                context = {"title": entry}
                return render(request, "encyclopedia/entryalreadyexists.html", context)
        if title is not None:
            content = request.POST.get("content")
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse(wiki_entry, args=(title,)))

    return render(request, "encyclopedia/addentry.html")


#Edit a particular entry.
def edit_entry(request, title):
    if request.method == "POST":
        if title is not None:
            content = request.POST.get("content")
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse(wiki_entry, args=(title,)))

    content = util.get_entry(title)
    context = {"title": title , "content": content}
    return render(request, "encyclopedia/editentry.html", context)


#A Random Page from the list.
def random_entry(request):
    entry_list=util.list_entries()
    if entry_list:
        title = random.choice(entry_list)
        return HttpResponseRedirect(reverse(wiki_entry, args=(title,)))
        #return HttpResponseRedirect(reverse("wiki_entry", args=(title,))) ,Here this
        #returns an URL while above one redirects to view function.
        #If you need to use something similar to the url template tag in your code, 
        #you can use reverse (). This function helps avoid having to hardcode a URL
        # in the view function.Here, it returns url with name "wikientry".
        #And, HttpResponseRedirect redirects it to that url with title as argument.Here,
        #we pass argument as tuple.