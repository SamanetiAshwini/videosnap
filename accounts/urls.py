from django.contrib.auth import admin
from .import views
from django.urls import path
urlpatterns = [
    path('home/', views.home,name='home'),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("profile/", views.profile, name="profile"),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    path("change-password/", views.change_password, name="change_password"),
    path("services/", views.services, name="services"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("faq/", views.faq, name="faq"),
    path("help/", views.help_page, name="help"),
    path("notifications/", views.notifications, name="notifications"),
    path("settings/", views.settings, name="settings"),
    path("privacy/", views.privacy, name="privacy"),
    path("terms/", views.terms, name="terms"),
    path("gallery/", views.gallery, name="gallery"),
    path("blog/", views.blog, name="blog"),
    path("blog-detail/", views.blog_detail, name="blog_detail"),
    path("search/", views.search, name="search"),
    path("results/", views.results, name="results"),
    path("add/",views.add,name="add"),
    path("sub/",views.sub,name="sub"),
    path("mul/",views.mul,name="mul"),
    path("div/",views.div,name="div"),
    path("sq/",views.sq,name="sq"),
]



