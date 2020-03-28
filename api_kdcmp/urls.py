from django.urls import include, path
from  rest_framework import routers
# from tutorial.quickstart import views
from api_kdcmp import views

router = routers.DefaultRouter()
router.register(r'villages', views.villagenameViewSet)
router.register(r'complaints', views.complaintsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    #  # path('', include('complaints.urls')),
]
