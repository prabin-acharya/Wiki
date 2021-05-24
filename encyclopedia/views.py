from django.shortcuts import render, redirect
from django import forms

from . import util

#    search = forms.CharField(label="", 
#        widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))

#class AddPageForm(forms.Form):
#    title = forms.CharField(label="Title : ", 
#        widget=forms.TextInput(attrs={'placeholder': 'Enter Title of the page'}))
#    newpage = forms.CharField(label="", 
#        widget=forms.Textarea(attrs={'placeholder': 'Type article here.'}))


def index(request):
    entry_list = util.list_entries()
    if request.method == "POST":
        search = request.POST.get("search")

        if search is not None:
            search = search.lower().strip()
            for entry in entry_list:
                if search == entry.lower():
                    return redirect('titlepageview', title=entry)
    

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


def addpage_view(request):
    context = {"searchform": SearchForm()}
    return render(request, "encyclopedia/addpage.html", context)



