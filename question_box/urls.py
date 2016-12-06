from django.conf.urls import url, include
from django.contrib import admin
from question_app import views
from rest_framework import routers
from abilities import views


router = routers.DefaultRouter()
router.register(r'abilities', views.AbilitiesViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
