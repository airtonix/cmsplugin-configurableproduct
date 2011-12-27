import os

from setuptools import (
  setup,
  find_packages,
)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='djangocms-plugin-configurableproduct',
    version='0.0.1',
     classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    packages=find_packages(),
    install_requires=[
        'sorl-thumbnail',
        'django-shop',
    ],
    author='Pavel Zhukov',
    author_email='airtonix@gmail.com',
    description='DjangoCMS plugin for Configurable product for django-shop',
    long_description = read('README.md'),
    license='BSD',
    keywords='djangocms, django-shop, product',
    url='git://github.com/airtonix/djangocms-plugin-configurableproduct.git',
    include_package_data=True,
    zip_safe = False,
)
