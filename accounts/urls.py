from django.urls import path
from accounts import views as vw

urlpatterns = [
    path('user/register',vw.UserRegistrationView.as_view(),name='register'),
    path('user/activate/<id>/<token>',vw.UserActivateUser.as_view(),name='activate'),
    path('user/login',vw.UserLoginView.as_view(),name='login'),
    path('user/logout',vw.UserLogoutView.as_view(),name='logout'),
    path('user/send-otp',vw.UserSendOTPViews.as_view()),
    path('user/verify-otp',vw.UserVerifyOTPViews.as_view()),
    path('user/changepassword',vw.UserChangePasswordView.as_view()),    

    #CRUD for Users
    path('user/all',vw.UserGetAllView.as_view()),
    path('user/get',vw.UserGetView.as_view()),
    path('user/create',vw.UserPostView.as_view()),
    path('user/update',vw.UserPutView.as_view()),
    path('user/delete',vw.UserDeleteView.as_view()),
]