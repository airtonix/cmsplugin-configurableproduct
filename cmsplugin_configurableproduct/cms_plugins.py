from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from configurableproduct.models import CProduct as Product
from configurableproduct.models.producttypes import ProductType

from .models import (
  CProductTypesPlugin,
  CProductsPlugin,
)

class ProductCategories(CMSPluginBase):
    model = CProductTypesPlugin
    name = _("Product Types")
    render_template = "shop/plugins/configurable_product/product-types/base.html"

    def render(self, context, instance, placeholder):
        objects = Product.objects.filter(active=True)
        used_types = objects.values("type").distinct()
        types = ProductType.objects.filter(pk__in = used_types)
        context.update({'Types': types, })
        return context
plugin_pool.register_plugin(ProductCategories)


class CategoryProducts(CMSPluginBase):
    model = CProductsPlugin
    name = _("Products of Type")
    render_template = "shop/plugins/configurable_product/product-list/base.html"

    def render(self, context, instance, placeholder):

        products = Product.objects.filter(type__pk__in = instance.categories.all())
        context.update({
          "Products": products
        })
        return context

plugin_pool.register_plugin(CategoryProducts)
