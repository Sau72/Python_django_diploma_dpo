from django.urls import path
from app_shop.api import (
    CategoryListView,
    ProductListView,
    ProductFullListView,
    TagListView,
    ReviewCreateView,
    CategoryView,
    SalesListView,
    CatalogListView,
    ProductPopularListView,
    ProductLimitedListView,
)

app_name = "app_shop"

urlpatterns = [
    path("api/banners/", ProductListView.as_view(), name="banners"),
    path(
        "api/products/popular/",
        ProductPopularListView.as_view(),
        name="products_popular",
    ),
    path(
        "api/products/limited/",
        ProductLimitedListView.as_view(),
        name="products_limited",
    ),
    path("api/product/<int:pk>/", ProductFullListView.as_view(), name="product"),
    path(
        "api/product/<int:pk>/review/",
        ReviewCreateView.as_view(),
        name="product_review",
    ),
    path(
        "api/product/<int:pk>/reviews",
        ReviewCreateView.as_view(),
        name="product_update_review",
    ),
    path("api/tags/", TagListView.as_view(), name="tags"),
    path("api/categories/", CategoryView.as_view()),
    path("api/sales/", SalesListView.as_view(), name="sales"),
    path("api/catalog/", CatalogListView.as_view(), name="catalog"),
]
