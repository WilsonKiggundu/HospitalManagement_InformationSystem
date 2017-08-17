from django.conf.urls import url

import app.views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'login/$', app.views.login, name='login'),
    url(r'logout/$', app.views.logout, name='logout'),
    url(r'^$', app.views.home, name='home'),
    url(r'^users/create/$', app.views.create_user, name='users/create')
]
