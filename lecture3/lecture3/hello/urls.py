from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("joe", views.joe, name="joe"),
    path("<str:name>", views.greet, name="greet")
]
