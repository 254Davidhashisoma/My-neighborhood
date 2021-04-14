
from django.conf.urls import url
from django.contrib.auth import login as auth_login,logout as auth_logout
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout


urlpatterns=[
    url( r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url('^$',views.home,name = 'home'),
    url(r'^profile/', views.profile, name='profile'),
    url('^neighbourhood', views.neighbourhood, name='neighbourhood'),
    url('^addneighbourhood',views.addneighbourhood,name="addneighbourhood"),
    url(r'^detail/(?P<neighbourhood_id>\d+)/$' , views.neighbourhood_details, name='detail' ),
    url(r'^new_business/(?P<pk>\d+)$',views.new_business,name='new_business'),
    url(r'^new_post/(?P<pk>\d+)$',views.new_post,name='new_post'),
    url(r'^search/',views.search_hoods,name='search_hoods'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)