from django.http.response import HttpResponse
from django.shortcuts import render
import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_markdown = util.get_entry(title)
    if entry_markdown:
        return HttpResponse(f"This is the entry for {title}!<br> {markdown2.markdown(entry_markdown)}")
    else:
        return HttpResponse(f"No entry found for for {title}!")
    # return render(request, "hello/greet.html", {
        # this is the context, all the variables passed to the template
    #    "name": name.capitalize()
    # })