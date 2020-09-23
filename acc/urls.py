from django.urls import path

from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [

    path('', views.index),

    path('verifyotp/', views.verifyotp, name='verifyotp'),

    path('verifyotp2/', views.verifyotp2, name='verifyotp2'),

    path('nik/', views.nik, name='nik'),

    path('nik2/', views.nik2, name='nik2'),

    path('recharge/', views.index1, name='index1'),

    path('contact/', views.contact, name='contact'),
    path('callback/', views.callback, name='callback'),

    path('logout/', views.logoutt, name='logout'),
    path('home/', views.home, name='home'),
    
    path('error/', views.error, name='error'),

    path('pay/', views.pay, name='pay'),
    path('paytm/', views.paytm, name='paytm'),

    path('orders/', views.index2, name='index2'),

    path('handlerequests/', views.handlerequests, name='handlerequests'),

]



if settings.DEBUG:

        urlpatterns += static(settings.MEDIA_URL,

                              document_root=settings.MEDIA_ROOT)