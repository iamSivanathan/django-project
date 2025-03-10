from django.urls import path # type: ignore
from . import views
from .views import login_view, logout_view


urlpatterns = [
     path('', views.index, name='index'),
     path('home/', views.home, name='home'),

     path('standing/', views.standing, name='standing'),
          path('standadd/',views.standadd,name='standadd'),
          path('standform/<int:pk>',views.standform,name='standform'),

     path('player/', views.player, name='player'),
          path('add/',views.add,name='add'),
          path('update/<int:pk>',views.update,name='update'),
          path('remove/<int:pk>',views.remove,name='remove'),

     path('team/', views.team, name='team'),
          path('beng/',views.beng, name='beng'),
          path('chen/',views.chen,name='chen'),
          path('ebeng/',views.e_beng,name='ebeng'),
          path('goa/',views.goa,name='goa'),
          path('hyd/',views.hyd,name='hyd'),
          path('jams/',views.jams,name='jams'),
          path('kerala/',views.kerala,name='kerala'),
          path('moham/',views.moham,name='moham'),
          path('mohun/',views.mohun,name='mohun'),
          path('mumbai/',views.mumbai,name='mumbai'),
          path('NE/',views.NE,name='NE'),
          path('odis/',views.odis,name='odis'),
          path('punj/',views.punj,name='punj'),



     path('login/', login_view, name='login'),
     path('logout/', logout_view, name='logout'),

]