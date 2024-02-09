from django.urls import path, include
from rest_framework import routers
from api_v1.views import PublicationViewSet, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_v1'

router = routers.DefaultRouter()
router.register(r'publications', PublicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

