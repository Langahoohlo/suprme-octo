from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

urlpatterns = [
    path('', include('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
    path('sms/', include('sms_receiver.urls')),
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
    path('static/<path:path>/', serve, {'document_root': settings.STATIC_ROOT}),
]

# if settings.DEBUG:
#     urlpatterns += static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
