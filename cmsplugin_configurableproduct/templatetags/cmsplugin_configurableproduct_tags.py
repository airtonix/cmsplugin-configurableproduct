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
        default_image_path = os.path.join(settings.STATIC_ROOT,
            ApplicationSettings.DEFAULT_CATEGORY_IMAGE_PATH)

        try:
            icon = product_type.icons.get(name = tag)

        except Exception, error:
            icon_file = open(default_image_path, 'r')
            icon = ImageFile(icon_file)

        except IOError, error:
            icon = None

        return icon
