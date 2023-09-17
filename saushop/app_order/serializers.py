from rest_framework import serializers
from app_order.models import Order, Payment
from app_shop.models import Product
from app_shop.serializers import ImageStringField, TagsStringField


class TagStringField(serializers.StringRelatedField):
    def to_representation(self, value):
        return {"id": value.pk, "name": str(value.name)}


class ImagesStringField(serializers.StringRelatedField):
    def to_representation(self, value):
        return {"src": str(value.src.url), "alt": str(value.pk)}


class BasketSerializer(serializers.ModelSerializer):
    images = ImageStringField(many=True, read_only=True)
    tags = TagsStringField(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "price",
            "count",
            "date",
            "title",
            "description",
            "freeDelivery",
            "images",
            "tags",
            "reviews",
            "rating",
        ]


class BasketUpdateSerializer(serializers.Serializer):
    id = serializers.CharField()
    count = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    products = BasketSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            "id",
            "createdAt",
            "fullName",
            "email",
            "phone",
            "deliveryType",
            "paymentType",
            "totalCost",
            "status",
            "city",
            "address",
            "products",
        ]


# class OrderConfSerializer(serializers.ModelSerializer):
#     fullName = serializers.CharField()
#     email = serializers.EmailField()
#     phone = serializers.CharField()
#     products = BasketSerializer(many=True)
#     paymentType = serializers.SlugField()
#
#     class Meta:
#         model = Product
#         fields = [
#             'id',
#             'createdAt',
#             'fullName',
#             'email',
#             'phone',
#             'deliveryType',
#             'paymentType',
#             'totalCost',
#             'status',
#             'city',
#             'address',
#             'products',
#         ]


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ["name", "number", "year", "month", "code"]


class UpdateOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "fullName",
            "email",
            "phone",
            "deliveryType",
            "paymentType",
            "totalCost",
            "status",
            "city",
            "address",
        ]
