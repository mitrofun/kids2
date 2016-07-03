from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from dashboard.views import DashboardView

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'', include('accounts.urls', namespace='accounts')),
    url(r'^children/', include('parameters.urls')),
    url(r'^children/', include('children.urls', namespace='children')),

    url(r'^dictionaries/', include('dictionaries.urls')),
    url(r'^admin/', include(admin.site.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
