
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from .views import HomeView, UserProductListView, ProductUpdate, ProductDetailView

urlpatterns = [
    path('user/', include('accounts.urls', namespace='users')),
    path('products/', UserProductListView.as_view(), name="product-list"),
    path('products/<slug>/', ProductDetailView.as_view(), name="product-detail"),
    path('products/<slug>/update', ProductUpdate.as_view(), name="product-update"),
    path('marketplace/', include('marketplace.urls', namespace="marketplace"))
    path('market/', include('marketplace', namespace="marketplace"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
 