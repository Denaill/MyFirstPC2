from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import login, logout_then_login, password_reset_done, password_reset_confirm, password_reset_complete, password_reset

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^coupons/', include('coupons.urls', namespace='coupons')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^', include('shop.urls', namespace='shop')),
    url(r'^users/', include('usuarios.urls', namespace='users')),
    url(r'^accounts/login', login, {'template_name':'login.html'}, name='login'),
    url(r'^logout/', logout_then_login, name='logout'),
    url(r'^reset/password_reset', password_reset, {'template_name':'registration/password_reset_form.html', 
    'email_template_name':'registration/password_reset_email.html'}, 
    name='password_reset'),
    url(r'^reset/password_reset_done', password_reset_done, {'template_name':'registration/password_reset_done.html'}, 
    name = 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z \-]+)/(?P<token>.+)/$', password_reset_confirm, {'template_name':'registration/password_reset_confirm.html'},
    name='password_reset_confirm'),
    url(r'reset/done', password_reset_complete, {'template_name':'registration/password_reset_complete.html'},
    name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
