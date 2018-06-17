from django.conf.urls import url 

from . import views

app_name = "users"
urlpatterns = [
    url(
        regex=r'^explorer/$',
        view=views.ExplorerUsers.as_view(),
        name='explorer_users'
    ),
]
