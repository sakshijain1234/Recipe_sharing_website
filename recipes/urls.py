from django.urls import path
from . import views

urlpatterns = [
    path('add-recipe/',views.get_data),
    path('delete-recipe/<id>/',views.delete_recipe),
    path('update-recipe/<id>/',views.update_recipe),
    path('search-recipe/',views.search_recipe),
    path('login/',views.login_page),
    path('signup/',views.signup_page),
    path('logout/',views.logout_page),
]
