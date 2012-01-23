## djangoCMS/Shop Configurable Products Extension

This simple extension provides some plugins to display things about your
[django-shop configurable products](https://bitbucket.org/zeus/django-shop-configurableproduct).


## Requirements

* django-shop
* django-cms
* django-shop-configurableproduct
* And all the requirements the above three projects depend on.


## Installation

1. make sure you are using a python virtual environment

>    virtualenv ~/Dev/virtualenv/projectname
>    . ~/Dev/virtualenv/projectname/bin/activate
>    cd ~/Dev/projects/projectname/

2. install it from pypi

>    pip install cmsplugin-configurableproduct

3. or, install it from github

>    pip install git+https://github.com/airtonix/cmsplugin-configurableproduct


## Override Template

Choosing a template in the administration interface means that you
populate the following two relative paths (to any of your app template dirs)
with templates you desire to be made available.

* cmsplugin_configurableproduct/product-types/containers/
* cmsplugin_configurableproduct/product-types/items/
* cmsplugin_configurableproduct/products/containers/
* cmsplugin_configurableproduct/products/items/


For example, if your django project was at :

    ~/Dev/Django/MyProjectName/

And you had a django application named `SomethingSomethingSomething` at :

    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/

Then templates for this plugin could be found at :

    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_configurableproduct/product-types/containers/*.html
    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_configurableproduct/product-types/items/*.html
    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_configurableproduct/products/containers/*.html
    ~/Dev/Django/MyProjectName/SomethingSomethingSomething/templates/cmsplugin_configurableproduct/products/items/*.html

In fact, anywhere django looks for templates, you can place the following tree :

    /cmsplugin_configurableproduct
        /product-types
            /containers/
                /*.html
            /items/
                /*.html
        /products
            /containers/
                /*.html
            /items/
                /*.html


### Customising Templates

Templates in all groups are provided the context :

a CMSPlugin has many useful attributes for you to use, the main one
is `plugin.instance` a reference to the settings model.

>     plugin' :
>         An instance of CMSPlugin, which itself provides reference to either
>         of the settings models as outlined below.

#### base.html

base.html in the `cmsplugin_configurableproduct` directory is used to load the
selected template chosen in the administration interface.


#### ./product-types/containers/*.html, ./product-types/items/*.html 

templates here are provided the context :

>     plugin.instance
>          categories
>               Chosen categories (configurableproduct.ProductType) for this instance,
>
>          hide_empty_categories
>               Self explanitory, effected in the cms_plugin.
>
>          container_template
>               Chosen template for the list container. for loop occurs here.
>
>          item_template
>               Chosen template for each item in the list.
>


#### ./products/containers/*.html, ./products/items/*.html

templates here are provided the context :


>     plugin.instance
>          categories
>               Chosen categories (configurableproduct.ProductType) for this instance,
>
>          hide_empty_categories
>               Self explanitory, effected in the cms_plugin.
>
>          filter_product_attributes
>               Comma separated list of CProductField names on which to
>               effect a filter action of either Filter, or Exclude.
>
>          filter_action
>               The action to take on the filter attributes listed above.
>
>          container_template
>               Chosen template for the list container. for loop occurs here.
>
>          item_template
>               Chosen template for each item in the list.
>
>     Products
>        A list of configurable_product.CProduct(s) after filtering based on chosen
>        chosen categories (configurableproduct.ProductType)


## TemplateTags

Since this plugin also introduces a new model in order to associate an Icon with an 
object in the configurableproduct.ProductType model, I created the following template tag
to help pull the relevant url.



>     `{% load cmsplugin_configurableproduct_tags %}`
> 
>     `{% product_type_icon ProductTypeObject '<ProductTypeIcon.name>' %}`



## Contributions

anyone is free to contribute, simply submit a merge request at
github : http://github.com/airtonix/cmsplugin-configurableproduct


## Todo

provide option to manipulate menu choices:

* Create block tag or filter `withproduct_type_icon` that exports url as a variable 
  for use with other templatetags.
* Refine the product filter.
* Provide better default templates.
* Allow selecting/use of snippets for menu templates?
