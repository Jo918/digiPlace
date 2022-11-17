
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include
from .views import HomeView, UserLibraryView, successView, stripe_webhook, UserProductListView, ProductUpdate, ProductDetailView, CreateCheckoutSessionView, ProducDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path('user/', include('accounts.urls', namespace='users')),

    path('create-checkout-session/<slug>/',
         CreateCheckoutSessionView.as_view(), name="create-checkout-session"),
    
    path('success/', successView.as_view(), name="success"),
    path("webhooks/stripe/", stripe_webhook, name="stripe-webhook"),
    path("library/<username>/", UserLibraryView.as_view(), name="library"),
    
    path('', HomeView.as_view(), name="home" ),
    path('products/', UserProductListView.as_view(), name="product-list"),
    path('products/<slug>/', ProductDetailView.as_view(), name="product-detail"),
    path('products/<slug>/update', ProductUpdate.as_view(), name="product-update"),
    
    path('products/<slug>/delete', ProducDeleteView.as_view(), name="product-delete"),

    path('marketplace/', include('marketplace.urls', namespace="marketplace"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.STATIC_ROOT)
 