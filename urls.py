
# from django.contrib import admin
# from django.urls import path,include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from shop.views import*



# urlpatterns =[
#     path('admin/', admin.site.urls),
#     path('shop/', include('shop.urls')),  
# ] 
# if settings.DEBUG:  # Serve media files only in development
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')), 
     path('login_page/', views.login_page, name='login_page'),
    path('register_page/', views.register_page, name='register_page'),
     path('new_recepie', views.recepie, name='recepie'),
    path('delete_receipe/<int:id>/', views.delete_receipe, name='delete_receipe'),
    path('update_receipe/<int:id>/', views.update_receipe, name='update_receipe'),
    path('logout_page/',views.logout_page,name='logout_page')
 # Includes shop URLs under /shop/
]

if settings.DEBUG:  # Serve media files only in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
