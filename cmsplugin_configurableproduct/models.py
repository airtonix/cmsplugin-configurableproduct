import os
from os.path import join, getsize

from django.db import models
from django.template.loader import get_template
from django.template.loaders.app_directories import app_template_dirs
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

from cms.models.pluginmodel import CMSPlugin

from .lib.choices import DynamicChoice


TEMPLATE_BASE_PATH = "cmsplugin_configurableproduct"
PRODUCT_TYPE_TEMPLATE_PATH = os.path.join(TEMPLATE_BASE_PATH, "product-types")
PRODUCT_LIST_TEMPLATE_PATH = os.path.join(TEMPLATE_BASE_PATH, "product-list")


class DynamicTemplateChoices(DynamicChoice):
    path = None
    exclude = None
    inlude = None

    def __init__(self, path=None, include=None,
                       exclude=None, *args, **kwargs):

        super(DynamicTemplateChoices, self).__init__(self, *args, **kwargs)
        self.path = path
        self.include = include
        self.exlude = exclude

    def generate(self,*args, **kwargs):
        choices = list()

        for template_dir in app_template_dirs:
          results = self.walkdir(os.path.join(template_dir, self.path))
          if results:
              choices += results

        return choices

    def walkdir(self, path=None):
        output = list()

        if not os.path.exists(path):
            return None

        for root, dirs, files in os.walk(path):

            if self.include:
                files = filter(lambda x: self.include in x, files)

            if self.exlude:
                files = filter(lambda x: not self.exlude in x, files)

            for item in files :
                output += ( (
                    os.path.join(self.path, item),
                    os.path.splitext(item)[0],
                ),)

            for item in dirs :
                output += self.walkdir(os.path.join(root, item))

        return output



class CProductTypesPlugin(CMSPlugin):
    """ Stores options for cmsplugin that shows lists of ProductTypes
    """

    TEMPLATE_CHOICES = DynamicTemplateChoices(
            path=PRODUCT_TYPE_TEMPLATE_PATH,
            include='.html',
            exclude='base')

    categories = models.ManyToManyField('configurableproduct.ProductType',
      blank=True, null=True,
      help_text="""Restrict the output list to these selected categories.
      if none are selected then all will be shown.""")

    show_category_icon = models.BooleanField(default=False,
      help_text="Display the icon for each category?")

    hide_empty_categories = models.BooleanField(default=True,
      help_text="Hide product types that have no products?")

    template = models.CharField(choices=TEMPLATE_CHOICES,
      max_length=256, blank=True, null=True,
      help_text="""Select a template to render this
      list. Templates are stored in : {0}""".format(PRODUCT_TYPE_TEMPLATE_PATH))

    def __unicode__(self):
        return U"Types: {0}".format(self.categories.all())


class CProductsPlugin(CMSPlugin):
    """ Stores Options to display list of products from certain ProductTypes
    """
    FILTER_ACTIONS = (
        ("show", "Filter"),
        ("hide", "Exclude")
      )
    TEMPLATE_CHOICES = DynamicTemplateChoices(
            path=PRODUCT_LIST_TEMPLATE_PATH,
            include='.html',
            exclude='base')


    categories = models.ManyToManyField('configurableproduct.ProductType',
      help_text="""Restrict the output list to these selected categories.
      if none are selected then all will be shown.""")
    hide_empty_categories = models.BooleanField(default=True)

    filter_product_attributes = models.CharField(max_length=256,
      blank=True, null=True,
      help_text="""Comma separated list of product
      field names and values to check for. ie :
        on_sale, is_preorder, holds_litres""")

    filter_action = models.CharField(max_length=32,
      blank=True, null=True, choices = FILTER_ACTIONS,
      help_text="How to treat the filter verbs?")

    template = models.CharField(choices=TEMPLATE_CHOICES,
      max_length=256,
      blank=True, null=True, help_text="""Select a template to render this
      list. Templates are stored in : {0}""".format(PRODUCT_LIST_TEMPLATE_PATH))

    def __unicode__(self):
        return U"Types: {0}".format(",".join([ ctype.name for ctype in self.categories.all()]))
