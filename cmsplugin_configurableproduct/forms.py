from django.forms import ModelForm
from django.forms import ModelChoiceField, ChoiceField

from .lib.choices import (
  DynamicTemplateChoices,
  DynamicChoice,
  )

from .models import (
  CProductTypesPlugin,
  CProductsPlugin,
  ApplicationSettings,
)


class CProductTypesAdminForm(ModelForm):

    class Meta:
        model = CProductTypesPlugin

    def __init__(self, *args, **kwargs):
        super(CProductTypesAdminForm, self).__init__(*args, **kwargs)
        self.fields['container_template'].choices = DynamicTemplateChoices(
                     path = ApplicationSettings.PRODUCT_TYPE_CONTAINER_TEMPLATES,
                  include = '.html')
        self.fields['item_template'].choices = DynamicTemplateChoices(
                     path = ApplicationSettings.PRODUCT_TYPE_ITEM_TEMPLATES,
                  include = '.html')


class CProductsAdminForm(ModelForm):

    class Meta:
        model = CProductsPlugin

    def __init__(self, *args, **kwargs):
        super(CProductsAdminForm, self).__init__(*args, **kwargs)
        self.fields['container_template'].choices = DynamicTemplateChoices(
                     path = ApplicationSettings.PRODUCT_CONTAINER_TEMPLATES,
                  include = '.html')
        self.fields['item_template'].choices = DynamicTemplateChoices(
                     path = ApplicationSettings.PRODUCT_ITEM_TEMPLATES,
                  include = '.html')
