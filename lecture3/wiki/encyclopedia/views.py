import random

from django import forms
from django.core.exceptions import ValidationError
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import markdown2

from . import util

# ensure this entry does not already exist
def validate_unique_title(title):
    if util.get_entry(title):
        raise ValidationError("An entry with this title already exists!")
    else:
        return title

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title", validators=[validate_unique_title])
    content = forms.CharField(label="Content", widget=forms.Textarea)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_markdown = util.get_entry(title)
    if entry_markdown:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": markdown2.markdown(entry_markdown)
        })
    else:
        return render(request, "encyclopedia/no_entry.html", {
            "title": title
        })

def search(request):
    query = request.GET.get('q', '')
    if util.get_entry(query):
        return redirect('entry', title=query)
    else:
        all_entries = util.list_entries()
        matches = filter(lambda x: query.lower() in x.lower(), all_entries)
        return render(request, "encyclopedia/search_results.html", {
            "query": query,
            "entries": matches
        })

def random_entry(request):
    all_entries = util.list_entries()
    random_entry = random.choice(all_entries)
    return redirect('entry', title=random_entry)

def new(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return redirect('entry', title=title)
        else:
            return render(request, "encyclopedia/new.html", {
                "form":form
            })
  
    return render(request, "encyclopedia/new.html", {
        "form": NewEntryForm()
    })