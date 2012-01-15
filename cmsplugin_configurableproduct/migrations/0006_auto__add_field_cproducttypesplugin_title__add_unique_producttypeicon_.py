# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'CProductTypesPlugin.title'
        db.add_column('cmsplugin_cproducttypesplugin', 'title', self.gf('django.db.models.fields.CharField')(default='Categories', max_length=128, null=True, blank=True), keep_default=False)

        # Adding unique constraint on 'ProductTypeIcon', fields ['product_type', 'name']
        db.create_unique('cmsplugin_configurableproduct_producttypeicon', ['product_type_id', 'name'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'ProductTypeIcon', fields ['product_type', 'name']
        db.delete_unique('cmsplugin_configurableproduct_producttypeicon', ['product_type_id', 'name'])

        # Deleting field 'CProductTypesPlugin.title'
        db.delete_column('cmsplugin_cproducttypesplugin', 'title')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_configurableproduct.cproductsplugin': {
            'Meta': {'object_name': 'CProductsPlugin', 'db_table': "'cmsplugin_cproductsplugin'", '_ormbases': ['cms.CMSPlugin']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['configurableproduct.ProductType']", 'symmetrical': 'False'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'filter_action': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'filter_product_attributes': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'hide_empty_categories': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'cmsplugin_configurableproduct.cproducttypesplugin': {
            'Meta': {'object_name': 'CProductTypesPlugin', 'db_table': "'cmsplugin_cproducttypesplugin'", '_ormbases': ['cms.CMSPlugin']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductType']", 'null': 'True', 'blank': 'True'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'hide_empty_categories': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Categories'", 'max_length': '128', 'null': 'True', 'blank': 'True'})
        },
        'cmsplugin_configurableproduct.producttypeicon': {
            'Meta': {'unique_together': "(('product_type', 'name'),)", 'object_name': 'ProductTypeIcon'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'small'", 'max_length': '128'}),
            'product_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'icons'", 'to': "orm['configurableproduct.ProductType']"})
        },
        'configurableproduct.productbooleanfield': {
            'Meta': {'object_name': 'ProductBooleanField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'configurableproduct.productcharfield': {
            'Meta': {'object_name': 'ProductCharField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'configurableproduct.productfloatfield': {
            'Meta': {'object_name': 'ProductFloatField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'configurableproduct.productimagefield': {
            'Meta': {'object_name': 'ProductImageField'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'configurableproduct.producttype': {
            'Meta': {'object_name': 'ProductType'},
            'boolean_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductBooleanField']", 'null': 'True', 'through': "orm['configurableproduct.TypeBoolean']", 'blank': 'True'}),
            'char_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductCharField']", 'null': 'True', 'through': "orm['configurableproduct.TypeChar']", 'blank': 'True'}),
            'float_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductFloatField']", 'null': 'True', 'through': "orm['configurableproduct.TypeFloat']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_fields': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['configurableproduct.ProductImageField']", 'null': 'True', 'through': "orm['configurableproduct.TypeImage']", 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        },
        'configurableproduct.typeboolean': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeBoolean'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductBooleanField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        },
        'configurableproduct.typechar': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeChar'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductCharField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        },
        'configurableproduct.typefloat': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeFloat'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductFloatField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        },
        'configurableproduct.typeimage': {
            'Meta': {'ordering': "['order']", 'object_name': 'TypeImage'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductImageField']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['configurableproduct.ProductType']"})
        }
    }

    complete_apps = ['cmsplugin_configurableproduct']
