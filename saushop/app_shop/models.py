from django.db import models
from app_profile.models import Profile


def category_preview_directory_path(instance: "Image", filename: str) -> str:
    return "category/{filename}".format(
        filename=filename,
    )


class ImageCategory(models.Model):
    src = models.ImageField(
        null=True,
        blank=True,
        upload_to=category_preview_directory_path,
        verbose_name="картинка",
    )
    alt = models.CharField(max_length=30, verbose_name="инфо картинки")

    class Meta:
        verbose_name = "image"
        verbose_name_plural = "images"

    def __str__(self):
        return self.alt


class Subcategory(models.Model):
    title = models.CharField(max_length=30, verbose_name="подкатегория")
    image = models.ForeignKey(ImageCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "subcategory"
        verbose_name_plural = "subcategory"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name="категория")
    image = models.ForeignKey(ImageCategory, on_delete=models.PROTECT)
    subcategories = models.ManyToManyField(Subcategory, related_name="category")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "category"

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.PROTECT,
        verbose_name="категория товара",
    )
    price = models.DecimalField(
        max_digits=1000000,
        default=0,
        blank=False,
        decimal_places=2,
        verbose_name="цена",
    )
    count = models.PositiveIntegerField(
        default=0, blank=False, verbose_name="количество"
    )
    date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True, verbose_name="дата создания"
    )
    title = models.CharField(max_length=128, verbose_name="название товара")
    description = models.TextField(
        max_length=2000, blank=True, null=False, verbose_name="описание товара"
    )
    fullDescription = models.TextField(
        max_length=3000, blank=True, verbose_name="полное описание"
    )
    freeDelivery = models.BooleanField(default=True, verbose_name="категория активна")
    reviews = models.IntegerField(default=0, blank=False, verbose_name="отзыв")
    rating = models.DecimalField(
        max_digits=100, default=0, blank=False, decimal_places=2, verbose_name="рейтинг"
    )
    sold_amount = models.PositiveSmallIntegerField(
        default=0, verbose_name="количество проданного товара"
    )

    class Meta:
        ordering = ["-sold_amount"]
        db_table = "product"
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return f"{self.title} - {self.price} руб."


class Review(models.Model):
    author = models.CharField(verbose_name="Автор", max_length=25, null=True)
    email = models.EmailField(max_length=100, verbose_name="Email")
    text = models.TextField(verbose_name="Содержание", max_length=255, null=True)
    rate = models.FloatField(null=True, default=0, verbose_name="Рейтинг")
    date = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True, null=True
    )
    user = models.ForeignKey(
        Profile,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="review", blank=True, null=True
    )

    def __str__(self):
        # return f'{self.rate}'
        return f"{self.product}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "reviews"
        db_table = "comments"


class Tag(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="tags", blank=True, null=True
    )
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
        db_table = "specification_names"


class Specification(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="specifications",
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=32, null=False, verbose_name="Название")
    value = models.CharField(max_length=32, null=False, verbose_name="Значение")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "specification"
        verbose_name_plural = "specifications"
        db_table = "specifications"


class ImageProduct(models.Model):
    src = models.ImageField(upload_to="image_product/", verbose_name="изображение")
    alt = models.CharField(max_length=100, default="string")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="images", blank=True, null=True
    )
    sales = models.ForeignKey(
        "Sales", on_delete=models.PROTECT, related_name="images", blank=True, null=True
    )

    def __str__(self):
        return f"{self.product}"

    class Meta:
        verbose_name = "imageProduct"
        verbose_name_plural = "ImageProducts"


# class Basket(models.Model):
#     product = models.ForeignKey(
#         Product,
#         related_name="product",
#         on_delete=models.PROTECT,
#         verbose_name="Продукт",
#     )
#     price = models.DecimalField(
#         max_digits=1000000,
#         default=0,
#         blank=False,
#         decimal_places=2,
#         verbose_name="цена",
#     )
#     count = models.PositiveIntegerField(
#         default=0, blank=False, verbose_name="количество"
#     )
#
#     class Meta:
#         ordering = ["-product"]
#         verbose_name = "basket"
#         verbose_name_plural = "baskets"
#
#     def __str__(self):
#         return f"Basket {self.product}"


class Sales(models.Model):
    price = models.DecimalField(
        max_digits=1000000,
        default=0,
        blank=False,
        decimal_places=2,
        verbose_name="цена",
    )
    salePrice = models.DecimalField(
        max_digits=1000000,
        default=0,
        blank=False,
        decimal_places=2,
        verbose_name="цена со скидкой",
    )
    dateFrom = models.DateField(blank=True, null=True, verbose_name="дата начала")
    dateTo = models.DateField(blank=True, null=True, verbose_name="дата конца")
    title = models.CharField(max_length=128, verbose_name="Заголовок")
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="продукт"
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "sale"
        verbose_name_plural = "sales"

    def __str__(self):
        return f"{self.product}"
