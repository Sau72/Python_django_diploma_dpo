from django.contrib import admin
from app_shop.models import (
    Product,
    Review,
    Specification,
    Tag,
    ImageProduct,
    ImageCategory,
    Subcategory,
    Category,
    Sales,
)

from app_order.models import Basket


class ReviewTabularInline(admin.TabularInline):
    model = Review
    extra = 0


class ImageProductTabularInline(admin.TabularInline):
    model = ImageProduct


class SpecificationTabularInline(admin.TabularInline):
    model = Specification


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "product"]
    list_display_links = ["id"]
    search_fields = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "category",
        "price",
        "count",
        "date",
        "description",
        "fullDescription",
        "freeDelivery",
        "reviews",
        "rating",
        "sold_amount",
    ]
    list_display_links = ["title"]
    inlines = [
        ImageProductTabularInline,
        SpecificationTabularInline,
        ReviewTabularInline,
    ]


@admin.register(ImageCategory)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["id", "src", "alt"]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image"]


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "price",
        "salePrice",
        "dateFrom",
        "dateTo",
    ]
    list_display_links = ["title"]
    inlines = [
        ImageProductTabularInline,
    ]
