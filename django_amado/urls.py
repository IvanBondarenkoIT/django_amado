"""django_amado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path-*7('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from account.views import login_view, logout_view, registration_view

app_name = 'django_amado'


urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('registration/', registration_view, name='registration_view'),

    path('admin/', admin.site.urls),
    path('', include('home.urls')),

    path('shop/', include('shop.urls', namespace='shop')),
    path('product/', include('product.urls', namespace='product')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('checkout/', include('checkout.urls', namespace='checkout')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

