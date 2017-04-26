from django.conf.urls import url
from membership import views as membershipviews

app_name = 'membership'

urlpatterns = [
    url(r'^$', membershipviews.user_login, name='login'),
    url(r'^logout/$', membershipviews.user_logout, name='logout'),

]
