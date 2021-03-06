from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import DingView, UserView, LevelView, UsersNearEdisonView
from .views import UsersNearby, YoView

urlpatterns = patterns('main.views',
    url(r'^$', 'index'),
    url(r'^ding/$', DingView.as_view()),
    url(r'^user/$', UserView.as_view()),
    url(r'^users_near_edison/$', UsersNearEdisonView.as_view()),
    url(r'^users_nearby/$', UsersNearby.as_view()),
    url(r'^level/$', LevelView.as_view()),
    url(r'^yo/$', YoView.as_view()),
)
