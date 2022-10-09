from .views import SubscriptionView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('create', SubscriptionView, basename='create')
urlpatterns = router.urls