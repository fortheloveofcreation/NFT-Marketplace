from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
	path('dashboard/', views.product_list, name='product_list'),
	#path('', views.home, name='home'),
	path('cart/', views.view_cart, name='view_cart'),
	path('checkout/', views.checkout, name='checkout'),
	path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
	path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
	path('', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view')
]
