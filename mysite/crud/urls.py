from django.urls import path
from . import views
urlpatterns=[
    path("",views.add_show,name="addshow"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("<int:id>/",views.update,name="update"),
]