"""Gateway URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path("admin/", admin.site.urls),
    path('Login/', views.login,name="Login"),
    path('Changepassword/', views.changepassword,name="change"),
    path('footer/', views.footer),
    path('forgot/', views.forgot, name="forgot"),
    path('', views.header,name="header"),
    path('help/', views.help,name="help"),
    path('registration/', views.registration,name="register"),
    path('review/', views.review,name="review"),
    path('sidebar/', views.sidebar),
    path('contact/', views.contact,name="contact"),
    path('base/', views.base),
    path('profile/', views.myprofile, name="profile"),
    path('logout/',views.logout,name="logout"),
    path('viewarticle/',views.viewarticle,name="viewarticle"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('hdianalysis/',views.hdianalysis,name="hdianalysis"),
    path('hdiprediction/',views.hdiprediction,name="hdiprediction"),
    path('Gnianalysis/',views.Gnianalysis,name="Gnianalysis"),
    path('Gniprediction/',views.Gniprediction,name="Gniprediction"),
    path('lifeanalysis/',views.lifeanalysis,name="lifeanalysis"),
    path('lifeprediction/',views.lifeprediction,name="lifeprediction"),
    path('happanalysis/',views.happanalysis,name="happanalysis"),
    path('happprediction/',views.happprediction,name="happprediction"),
    path('g1/',views.g1,name="g1"),
    path('g2/',views.g2,name="g2"),
    path('g3/',views.g3,name="g3"),
    path('g4/',views.g4,name="g4"),
    path('g5/',views.g5,name="g5"),
    path('g6/',views.g6,name="g6"),
    path('g7/',views.g7,name="g7"),
    path('g8/',views.g8,name="g8"),
    path('g9/',views.g9,name="g9"),
    path('g10/',views.g10,name="g10"),
    path('h1/',views.h1,name="h1"),
    path('h2/',views.h2,name="h2"),
    path('h3/',views.h3,name="h3"),
    path('h4/',views.h4,name="h4"),
    path('h5/',views.h5,name="h5"),
    path('h6/',views.h6,name="h6"),
    path('h7/',views.h7,name="h7"),
    path('h8/',views.h8,name="h8"),
    path('h9/',views.h9,name="h9"),
    path('h10/',views.h10,name="h10"),
    path('hdi1/',views.hdi1,name="hdi1"),
    path('hdi2/',views.hdi2,name="hdi2"),
    path('hdi3/',views.hdi3,name="hdi3"),
    path('hdi4/',views.hdi4,name="hdi4"),
    path('hdi5/',views.hdi5,name="hdi5"),
    path('hdi6/',views.hdi6,name="hdi6"),
    path('hdi7/',views.hdi7,name="hdi7"),
    path('hdi8/',views.hdi8,name="hdi8"),
    path('hdi9/',views.hdi9,name="hdi9"),
    path('hdi10/',views.hdi10,name="hdi10"),
    path('L1/',views.L1,name="L1"),
    path('L2/',views.L2,name="L2"),
    path('L3/',views.L3,name="L3"),
    path('L4/',views.L4,name="L4"),
    path('L5/',views.L5,name="L5"),
    path('L6/',views.L6,name="L6"),
    path('L7/',views.L7,name="L7"),
    path('L8/',views.L8,name="L8"),
    path('L9/',views.L9,name="L9"),
    path('L10/',views.L10,name="L10"),
    path('Astudy/',views.Astudy,name="Australia"),
    path('latestnews/',views.latestnews,name="latestnews"),
    path('viewcountries/',views.viewcountries,name="viewcountries"),
    path('countrydetails/<str:name>',views.countrydetails,name="countrydetails"),
    path('ilets/',views.it,name="ilets"),
    path('pte/',views.pte,name="pte"),
    path('spoken/',views.spoken,name="spoken"),
    path('sat/',views.sat,name="sat"),
    path('Visa/',views.viewvisa,name="Visa"),
    path('find/',views.find,name="find"),
    path('tips/',views.tips,name="tips"),
    path('about/',views.about,name="about"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('artdetail/<int:id>',views.artdetail,name="artdetail"),
    path('viewvideo/',views.viewvideo,name="viewvideo"),
    path('viewvisadetail/<str:name>',views.viewvisadetail,name="viewvisadetail"),
    path('viewuni/',views.viewuni,name="viewuni")




]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
