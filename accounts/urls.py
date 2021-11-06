from django.urls import path
from . import views
from django.contrib.auth import views as pass_views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('reset_password/',pass_views.PasswordResetView.as_view(), name="reset_password"),
    # we can write pass_views.PasswordResetView.as_view(template_name='our name')
    path('reset_password_sent/',pass_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #token is to check the password is valid
    path('reset/<uidb64>/<token>',pass_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #uidb64 user id encoded in base64
    path('reset_password_complete/',pass_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]

# '''
# 1 - Submit email form                         //PasswordResetView.as_view()
# 2 - Email sent success message                //PasswordResetDoneView.as_view()
# 3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
# 4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
# '''