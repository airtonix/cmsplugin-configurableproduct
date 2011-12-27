import os

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from configurableproduct.models import CProduct as Product
from configurableproduct.models.producttypes import ProductType

from .models import (
  CProductTypesPlugin,
  CProductsPlugin,
  TEMPLATE_BASE_PATH,
  PRODUCT_TYPE_TEMPLATE_PATH,
  PRODUCT_LIST_TEMPLATE_PATH,
)

class ProductCategories(CMSPluginBase):
    model = CProductTypesPlugin
    name = _("List of Product Types")
    render_template = os.path.join(TEMPLATE_BASE_PATH, "base.html")
    default_template = os.path.join(PRODUCT_TYPE_TEMPLATE_PATH, "default.html")
    admin_preview = False

    def render(self, context, instance, placeholder):
        objects = Product.objects.filter(active=True)
        used_types = objects.values("type").distinct()
        types = ProductType.objects.filter(pk__in = used_types)

        context.update({
          'Types': types,
          'Template' : instance.template if instance.template else self.default_template
        })

        return context


plugin_pool.register_plugin(ProductCategories)


class CategoryProducts(CMSPluginBase):
    model = CProductsPlugin
    name = _("List of Products")
    render_template = os.path.join(TEMPLATE_BASE_PATH, "base.html")
    default_template = os.path.join(PRODUCT_TYPE_TEMPLATE_PATH, "default.html")
    admin_preview = False

    def render(self, context, instance, placeholder):
        products = Product.objects.filter(type__pk__in = instance.categories.all())
        context.update({
          "Products": products,
          'Template' : instance.template if instance.template else self.default_template
        })
        return context

plugin_pool.register_plugin(CategoryProducts)
