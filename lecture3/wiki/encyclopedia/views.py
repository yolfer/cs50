import random
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
import markdown2

from . import util


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