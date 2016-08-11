from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', login_required(TemplateView.as_view(template_name='dashboard.html')), name='dashboard'),
    url(r'', include('accounts.urls', namespace='accounts')),
    url(r'^children/', include('children.urls', namespace='children')),
    url(r'^dictionaries/', include('dictionaries.urls', namespace='dictionaries')),
    url(r'^admin/', include(admin.site.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar

    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
