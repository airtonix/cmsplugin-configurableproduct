# -*- coding: utf-8 -*-
import os

from django import template
from django.conf import settings
from django.core.files.images import ImageFile


from classytags.helpers import InclusionTag
from classytags.core import Tag, Options
from classytags.arguments import (
  Argument,
)

from configurableproduct.models import CProduct
from configurableproduct.models.producttypes import ProductType

from ..models import (
  ProductTypeIcon,
  ApplicationSettings,
)

register = template.Library()


@register.tag()
class ProductTypeIcon(Tag):
    name="product_type_icon"
    options = Options(
        Argument('product_type', resolve=True, required=True),
        Argument('tag', resolve = True, required = True),
    )

    def render_tag(self, context, product_type, tag):
        try:
            icon= product_type.icons.get(name = tag)
            return settings.MEDIA_URL+str(icon.image)

        except Exception, error:
            return ApplicationSettings.DEFAULT_CATEGORY_IMAGE_URL.format(tag.lower())
