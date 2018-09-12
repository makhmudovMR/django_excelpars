from django.conf.urls import url
from .views import home, login_view, panel, logout_view

urlpatterns = [
    url('^$', home, name='home'),
    url('^login/$', login_view, name='login'),
    url('^panel/$', panel, name='page'),
    url('^logout/$', logout_view, name='logout')
]