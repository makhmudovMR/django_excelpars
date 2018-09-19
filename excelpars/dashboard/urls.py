from django.conf.urls import url
from .views import home, login_view, panel, logout_view, get_id_data, edit_data, add_data, search

urlpatterns = [
    url('^$', home, name='home'),
    url('^login/$', login_view, name='login'),
    url('^panel/$', panel, name='panel'),
    url('^logout/$', logout_view, name='logout'),
    url('^get_id_data/$', get_id_data, name='get_id_data'),
    url('^edit_data/$', edit_data, name='edit_data'),
    url('^add_data/$', add_data, name='add_data'),
    url('^search/$', search, name='search')
]