from django.conf.urls import patterns, url

urlpatterns = patterns('trainings.views',
        url(r'^type/(?P<type_id>\d*)/?$', 'display_type'),
        )
