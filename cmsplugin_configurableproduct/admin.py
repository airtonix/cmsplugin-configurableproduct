from django.contrib import admin
from django import forms
from django.template.defaultfilters import slugify

from configurableproduct.admin import CProductAdmin
from configurableproduct.admin import (
  ProductCharInline,
  ProductBooleanInline,
  ProductFloatInline,
  ProductImageInline
)

from configurableproduct.models import (
  ProductType,
  CProduct,
)

from models import (
  ProductTypeIcon,
)

class ProductTypeIconAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'name', 'image',  )
admin.site.register(ProductTypeIcon, ProductTypeIconAdmin)
