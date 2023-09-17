import json
import datetime
from math import ceil
from django.core.paginator import Paginator
from app_shop.models import Category, Product, Tag, Review, Sales
from app_order.models import Basket
from app_shop.serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductFullSerializer,
    TagSerializer,
    ReviewSerializer,
    SalesSerializer,
    CatalogSerializer,
)

from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView,
    ListCreateAPIView,
)
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import pagination
from django.db.models import Count


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductPopularListView(ListAPIView):
    queryset = Product.objects.filter(count__gte=50)
    serializer_class = ProductSerializer


class ProductLimitedListView(ListAPIView):
    queryset = Product.objects.filter(count__lte=50)
    serializer_class = ProductSerializer


class ProductFullListView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFullSerializer


class ReviewCreateView(APIView):
    def get(self, request):
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            product = Product.objects.get(pk=pk)
            review = Review.objects.create(
                author=serializer.data["author"],
                email=serializer.data["email"],
                text=serializer.data["text"],
                rate=serializer.data["rate"],
                date=datetime.datetime.now().strftime("%H:%M:%S"),
                product=product,
            )
            review.save()

            review = Review.objects.filter(product_id=pk).all()
            serializer = ReviewSerializer(review, many=True)
            return Response(serializer.data)


class TagListView(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryView(ListModelMixin, CreateModelMixin, GenericAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        return queryset

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class SalesListView(APIView):
    def get(self, data):
        queryset = Sales.objects.all()

        page_number = int(self.request.query_params.get("currentPage"))
        page_size = 20
        paginator = Paginator(queryset, page_size)

        serializer = SalesSerializer(paginator.page(page_number), many=True)

        serializer = {
            "items": serializer.data,
            "currentPage": page_number,
            "lastPage": ceil(len(queryset) / page_size),
        }
        return Response(serializer)


class CatalogListView(APIView):
    def get_queryset(self):
        category = self.request.META["HTTP_REFERER"].split("/")[4]

        if category.isdigit():
            queryset = Product.objects.filter(category_id=category)
        else:
            queryset = Product.objects.all()

        if self.request.query_params:
            name = self.request.query_params.get("filter[name]")
            if name:
                queryset = queryset.filter(title__icontains=name)

            min_price = self.request.query_params.get("filter[minPrice]")
            if min_price:
                queryset = queryset.filter(price__gte=min_price)

            max_price = self.request.query_params.get("filter[maxPrice]")
            if max_price:
                queryset = queryset.filter(price__lte=max_price)

            free_delivery = self.request.query_params.get("filter[freeDelivery]")
            if free_delivery == "true":
                queryset = queryset.filter(freeDelivery=True)

            available = self.request.query_params.get("filter[available]")
            if available and available == "true":
                queryset = queryset.filter(count__gte=1)

            sort_param = self.request.query_params.get("sort")
            sort_type = self.request.query_params.get("sortType")

            if sort_param == "reviews":
                queryset = queryset.annotate(cnt=Count("reviews"))

            if sort_type == "dec":
                queryset = queryset.order_by(f"-{sort_param}")
            else:
                queryset = queryset.order_by(sort_param)

            tags = dict(self.request.query_params).get("tags[]")
            if tags:
                prod_id = Tag.objects.filter(id__in=tags).values_list("product_id")
                queryset = queryset.filter(id__in=prod_id)
            return queryset

    def get(self, data):
        filtered_products = self.get_queryset()
        print(filtered_products)

        page_number = int(self.request.query_params.get("currentPage"))
        # page_size = 3
        page_size = int(self.request.query_params.get("limit"))
        paginator = Paginator(filtered_products, page_size)

        serializer = CatalogSerializer(paginator.page(page_number), many=True)

        serializer = {
            "items": serializer.data,
            "currentPage": page_number,
            "lastPage": ceil(len(filtered_products) / page_size),
        }
        return Response(serializer)
