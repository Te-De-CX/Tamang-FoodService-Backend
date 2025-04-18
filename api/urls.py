from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductsViewSet, OrderViewSet, CategoryViewSet, PaymentViewSet, ReviewViewSet,  ToggleFavoriteView, UserFavoritesViewSet, ChefsDataViewSet, AdsViewSet, UserViewSet, CurrentUserView, CartViewSet, OrderItemViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'chefsdata', ChefsDataViewSet)
router.register(r'ads', AdsViewSet)
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'orderitems', OrderItemViewSet, basename='orderitems')
router.register(r'favorites', UserFavoritesViewSet, basename='users-favourites' )

urlpatterns = [
    path('', include(router.urls)),
    # path('favorites/', UserFavoritesViewSet.as_view(), name='user-favorites-list'),
    path('favorites/toggle/<int:product_id>/', ToggleFavoriteView.as_view(), name='toggle-favorite'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('users/me/', CurrentUserView.as_view(), name='current-user'),
]