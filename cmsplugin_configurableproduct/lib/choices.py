import os

from django.contrib import admin
from django.template.loader import get_template
from django.template.loaders.app_directories import app_template_dirs
from django.core.exceptions import ImproperlyConfigured
from django.utils.importlib import import_module

#import settings
from formatting import deslugify

class DynamicChoice(object):
    """
    Trivial example of creating a dynamic choice
    """

    def __iter__(self, *args, **kwargs):
        for choice in self.generate():
            if hasattr(choice,'__iter__'):
                yield (choice[0], choice[1])
            else:
                yield choice, choice

    def __init__(self, *args, **kwargs):
        """
        If you do it here it is only initialized once. Then just return generated.
        """
        import random
        self.generated = [random.randint(1,100) for i in range(10)]

    def generate(self, *args, **kwargs):
        """
        If you do it here it is  initialized every time the iterator is used.
        """
        import random
        return [random.randint(1,100) for i in range(10)]



class DynamicTemplateChoices(DynamicChoice):
    path = None

    # exclude templates whose name includes these keywords
    exclude = None

    # only include templates whos name contains these keywords
    inlude = None

    #
    # TODO: Scan for snippets as well.
    #
    # scan for and include snippets in choices?
    #scan_snippets = False

    # snippets whose title prefixed with this moniker are considered to be
    # templates for our cmsplugin.

    #snippet_title_moniker = getattr(
    #  settings.CONFIGURABLEPRODUCT_CMSPLUGIN_SNIPPETS_MONIKER,
    #  "[configurableproduct-snippet]")


    def __init__(self, path=None, include=None,
                       exclude=None, *args, **kwargs):

        super(DynamicTemplateChoices, self).__init__(self, *args, **kwargs)
        self.path = path
        self.include = include
        self.exlude = exclude

    def generate(self,*args, **kwargs):
        choices = list(("-[ Nothing Selected ]-", ), )

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
                    deslugify(os.path.splitext(item)[0]),
                ),)

            for item in dirs :
                output += self.walkdir(os.path.join(root, item))

        return output
