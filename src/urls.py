from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from common.dashboard import DashboardView
from common.views import status_view
from loader.views import upload

admin.site.site_header = settings.ADMIN_SITE_HEADER

urlpatterns = [
    url(r'^$', login_required(DashboardView.as_view()), name='dashboard'),
    url(r'', include('accounts.urls', namespace='accounts')),

    url(r'^children/', include('children.urls', namespace='children')),
    url(r'^dictionaries/', include('dictionaries.urls', namespace='dictionaries')),
    url(r'^upload/$', login_required(upload), name='loader'),
    url(r'^reports/', include('reports.urls', namespace='reports')),
    url(r'^status/$', status_view, name="status"),
    url(r'^django-rq/', include('django_rq.urls')),
    url(r'^admin/', include(admin.site.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
