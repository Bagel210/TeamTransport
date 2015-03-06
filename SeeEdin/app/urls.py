from django.conf.urls import patterns, include, url
# from django.contrib import admin

from app.views import journeyPlan

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SeeEdin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','app.views.home'),
    #url(r'^app','app.views.app'),

    url(r'^app/$', journeyPlan, name="journey_planner"),

    # url(r'^/',include('app.urls')),
)
