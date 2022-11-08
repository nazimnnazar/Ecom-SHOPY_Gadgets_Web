from django import views
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),

    #cart
    path('cartDetails/', views.cartdetails, name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart'),
    path('min/<int:product_id>/', views.min_cart, name='mincart'),
    path('remove/<int:product_id>/', views.remove, name='remove'),
    #end Cart
    path('contact/',views.contact,name='contact'),
    path('checkout/',views.checkout,name='checkout'),
    # Account
    path('register/',views.register,name='register'),
    path('login/',views.signin,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('profile/',views.profile,name='profile'),
    #Accounts
    path('add/',views.add,name='add'),
    path('<slug:c_slug>/',views.home,name='prod'),
    path('<slug:c_slug>/<slug:product_slug>',views.views,name='views'),
    # path('cartsetails/',views.cartsetails,name='cartdetails'),
]
