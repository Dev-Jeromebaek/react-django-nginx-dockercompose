from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'items', views.ItemViewSet)

urlpatterns = router.urls
