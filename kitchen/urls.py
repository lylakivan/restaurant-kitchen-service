from django.urls import path

from kitchen.views import (
    index,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    DishDetailView,
    DishListView,
    DishCreateView,
    DishUpdateView
)


urlpatterns = [
    path("", index, name="index"),
    path("dish_types/", DishTypeListView.as_view(), name="dish_type-list"),
    path("dish_types/create", DishTypeCreateView.as_view(), name="dish_type-create"),
    path("dish_types/<int:pk>/update", DishTypeUpdateView.as_view(), name="dish_type-update"),
    path("dish_types/<int:pk>/delete", DishTypeDeleteView.as_view(), name="dish_type-delete"),

    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("cooks/create", CookCreateView.as_view(), name="cook-create"),

    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update", DishUpdateView.as_view(), name="dish-update"),

]

app_name = "kitchen"
