from django.urls import path
from . import views


app_name = 'todolist'
urlpatterns = [
    path("", view=views.index, name="index"),
    path("del/<int:task_id>", view=views.delete, name="delete"),
    path("create_page/", view=views.create_page, name="create_page"),
    path("update/<int:task_id>", view=views.update, name="update"),
    path("create/", view=views.create, name="create"),
]