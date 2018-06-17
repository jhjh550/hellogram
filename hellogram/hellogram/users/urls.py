from django.conf.urls import url 

from . import views

app_name = "users"
urlpatterns = [
    url(
        regex=r'^explorer/$',
        view=views.ExplorerUsers.as_view(),
        name='explorer_users'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/follow/$',
        view=views.FollowUser.as_view(),
        name='follow_users'
    ),
    url(
        regex=r'^(?P<user_id>[0-9]+)/unfollow/$',
        view=views.UnFollowUser.as_view(),
        name='unfollow_users'
    ),
]
