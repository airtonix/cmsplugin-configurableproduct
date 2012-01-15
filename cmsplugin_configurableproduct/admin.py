import os

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
  STATIC_URL
)

from pprint import pprint

class ProductTypeIconAdmin(admin.ModelAdmin):
    list_display = ('product_type', 'name', 'image_preview',  )

    def image_preview(self, obj):
        return U"""
          <span style='display:inline-block;margin:.5em;'>
            <img src='{url}' />
          </span>
          <pre style='display:inline-block;'>{url}</pre>
        """.format(url = obj.image.url)
    image_preview.allow_tags=True

admin.site.register(ProductTypeIcon, ProductTypeIconAdmin)
