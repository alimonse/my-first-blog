from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [#patrones de los URLs para llamar a esas pags web
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
]
