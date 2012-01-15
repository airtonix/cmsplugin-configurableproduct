import os
from os.path import join, getsize

from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

from cms.models.pluginmodel import CMSPlugin

from appconf import AppConf

from .lib.choices import (
  DynamicTemplateChoices,
  DynamicChoice,
  )

STATIC_URL = getattr(settings, "STATIC_URL", '/static')
STATIC_ROOT = getattr(settings, "STATIC_ROOT", None)
MEDIA_URL = getattr(settings, "MEDIA_URL", '/media')
MEDIA_ROOT = getattr(settings, "MEDIA_ROOT", None)


class ApplicationSettings(AppConf):
    TEMPLATE_BASE_PATH = __package__
    PRODUCT_TYPE_TEMPLATE_PATH = os.path.join(TEMPLATE_BASE_PATH, "product-types")
    PRODUCT_LIST_TEMPLATE_PATH = os.path.join(TEMPLATE_BASE_PATH, "product-list")
    DEFAULT_CATEGORY_IMAGE_URL = '{0}/defaults/img/product-category'.format(STATIC_URL)
    DEFAULT_CATEGORY_IMAGE_ROOT = '{0}/defaults/img/product-category'.format(STATIC_ROOT)
    CATEGORY_IMAGE_URL = '{0}/product-category'.format(MEDIA_URL)
    CATEGORY_IMAGE_ROOT = '{0}/product-category'.format(MEDIA_ROOT)

class ProductTypeIcon(models.Model):
#    upload_path = lambda instance, filename: "/product-category".join((
#      ApplicationSettings.CATEGORY_IMAGE_ROOT, "{0}-{1}".format(
#        slugify(instance.product_type), filename)))

    upload_path = lambda instance, filename: "files/product-category/{0}".format(
      "{0}-{1}".format(slugify(instance.product_type), filename) )

    # fields
    name = models.CharField(max_length=128, default="small")
    image = models.ImageField(upload_to=upload_path, blank=True, null=True)
    product_type = models.ForeignKey('configurableproduct.ProductType',
       related_name='icons', help_text="""The product type you want this icon
       related to...""")


class CProductTypesPlugin(CMSPlugin):
    """ Stores options for cmsplugin that shows lists of ProductTypes
    """
    TEMPLATE_CHOICES = DynamicTemplateChoices(
            path=ApplicationSettings.PRODUCT_TYPE_TEMPLATE_PATH,
            include='.html',
            exclude='base')
    DEFAULT_TEMPLATE = os.path.join(ApplicationSettings.PRODUCT_TYPE_TEMPLATE_PATH,
      "default.html")

    categories = models.ManyToManyField('configurableproduct.ProductType',
      blank=True, null=True,
      help_text="""Restrict the output list to these selected categories.
      if none are selected then all will be shown.""")

    hide_empty_categories = models.BooleanField(default=True,
      help_text="Hide product types that have no products?")

    template = models.CharField(choices=TEMPLATE_CHOICES,
      max_length=256, blank=True, null=True,
      help_text="""Select a template to render this
      list. Templates are stored in : {0}""".format(ApplicationSettings.PRODUCT_TYPE_TEMPLATE_PATH))

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
            path=ApplicationSettings.PRODUCT_LIST_TEMPLATE_PATH,
            include='.html',
            exclude='base')
    DEFAULT_TEMPLATE = os.path.join(ApplicationSettings.PRODUCT_LIST_TEMPLATE_PATH,
      "default.html")

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
      list. Templates are stored in : {0}""".format(ApplicationSettings.PRODUCT_LIST_TEMPLATE_PATH))

    def __unicode__(self):
        return U"Types: {0}".format(",".join([ ctype.name for ctype in self.categories.all()]))
