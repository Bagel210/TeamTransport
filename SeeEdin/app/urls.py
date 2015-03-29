from django.conf.urls import patterns, include, url
# from django.contrib import admin
from django.contrib.auth.decorators import login_required, permission_required

from app.views import journeyPlan, route, register, user_login, user_logout

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'SeeEdin.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^$', 'app.views.home'),

                       url(r'^Home/$', 'app.views.home'),

                       url(r'^app/$', login_required(journeyPlan), name="journey_planner"),
                       url(r'^app/route$', route, name="route"),

                       url(r'^register/$', register, name='register'),

                       url(r'^login/$', user_login, name='login'),

                       url(r'^logout/$', login_required(user_logout), name='logout'),

                       # url(r'^/',include('app.urls')),
)
