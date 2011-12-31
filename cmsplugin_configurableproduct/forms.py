from django.forms import ModelForm
from django.forms import ModelChoiceField, ChoiceField

from .lib.choices import (
  DynamicTemplateChoices,
  DynamicChoice,
  )

from .models import (
  CProductTypesPlugin,
  CProductsPlugin,
  TEMPLATE_BASE_PATH,
  PRODUCT_TYPE_TEMPLATE_PATH,
  PRODUCT_LIST_TEMPLATE_PATH,
)


class CProductTypesAdminForm(ModelForm):

    class Meta:
        model = CProductTypesPlugin

    def __init__(self, *args, **kwargs):
        super(CProductTypesAdminForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices = DynamicTemplateChoices(
                     path = PRODUCT_TYPE_TEMPLATE_PATH,
                  include = '.html',
                  exclude = 'base')


class CProductsAdminForm(ModelForm):

    class Meta:
        model = CProductsPlugin

    def __init__(self, *args, **kwargs):
        super(CProductsAdminForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices = DynamicTemplateChoices(
                     path = PRODUCT_LIST_TEMPLATE_PATH,
                  include = '.html',
                  exclude = 'base')
