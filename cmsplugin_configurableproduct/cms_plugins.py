import os

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin

from configurableproduct.models import CProduct as Product
from configurableproduct.models.producttypes import ProductType

from .lib.choices import (
  DynamicTemplateChoices,
  DynamicChoice,
  )

from .models import (
  CProductTypesPlugin,
  CProductsPlugin,
  ApplicationSettings,
)

from .forms import (
  CProductTypesAdminForm,
  CProductsAdminForm,
)

class ProductCategories(CMSPluginBase):
    model = CProductTypesPlugin
    name = _("List of Product Types")
    render_template = os.path.join(ApplicationSettings.TEMPLATE_BASE_PATH, "base.html")
    admin_preview = False
    form = CProductTypesAdminForm
    filter_horizontal = ('categories', )

    def render(self, context, instance, placeholder):

        types = ProductType.objects.all()

        if instance.hide_empty_categories :
            objects = Product.objects.filter(active=True)
            used_types = objects.values("type").distinct()
            types = types.filter(pk__in = used_types)

#        chosen_categories = instance.categories.all()
#        if chosen_categories.count() > 0:
#            types.filter(pk__in = instance.categories.values('id'))

        context.update({
          'Types': types,
        })

        return context
plugin_pool.register_plugin(ProductCategories)


class CategoryProducts(CMSPluginBase):
    model = CProductsPlugin
    name = _("List of Products")
    render_template = os.path.join(ApplicationSettings.TEMPLATE_BASE_PATH, "base.html")
    admin_preview = False
    form = CProductsAdminForm
    filter_horizontal = ('categories', )

    fieldsets = (
      ('Display Template',
          {'fields': [ ('template', ),
                      ]}),

      ('Show Products of Type...',
          {'fields': [ ('hide_empty_categories','categories', ),
                      ]}),

      ('Filtering', {
        'classes': ('collapse',),
        'fields': ['filter_action', 'filter_product_attributes']
      }),
    )

    def render(self, context, instance, placeholder):
        products = Product.objects.filter(type__pk__in = instance.categories.all())
        context.update({
          "Products": products,
        })
        return context

plugin_pool.register_plugin(CategoryProducts)
