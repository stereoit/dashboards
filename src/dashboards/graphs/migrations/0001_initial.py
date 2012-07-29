# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'KPI'
        db.create_table('graphs_kpi', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('values', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['graphs.KPIValue'])),
            ('history', self.gf('django.db.models.fields.IntegerField')(default=100)),
            ('granularity', self.gf('django.db.models.fields.IntegerField')(default=60)),
        ))
        db.send_create_signal('graphs', ['KPI'])

        # Adding model 'KPIValue'
        db.create_table('graphs_kpivalue', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('graphs', ['KPIValue'])

        # Adding model 'ColorPalette'
        db.create_table('graphs_colorpalette', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('graphs', ['ColorPalette'])

        # Adding M2M table for field colors on 'ColorPalette'
        db.create_table('graphs_colorpalette_colors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('colorpalette', models.ForeignKey(orm['graphs.colorpalette'], null=False)),
            ('color', models.ForeignKey(orm['graphs.color'], null=False))
        ))
        db.create_unique('graphs_colorpalette_colors', ['colorpalette_id', 'color_id'])

        # Adding model 'Color'
        db.create_table('graphs_color', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color', self.gf('colorful.fields.RGBColorField')(max_length=7)),
        ))
        db.send_create_signal('graphs', ['Color'])

        # Adding model 'Graph'
        db.create_table('graphs_graph', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kpi', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['graphs.KPI'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('palette', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['graphs.ColorPalette'])),
            ('graph_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('graphs', ['Graph'])


    def backwards(self, orm):
        # Deleting model 'KPI'
        db.delete_table('graphs_kpi')

        # Deleting model 'KPIValue'
        db.delete_table('graphs_kpivalue')

        # Deleting model 'ColorPalette'
        db.delete_table('graphs_colorpalette')

        # Removing M2M table for field colors on 'ColorPalette'
        db.delete_table('graphs_colorpalette_colors')

        # Deleting model 'Color'
        db.delete_table('graphs_color')

        # Deleting model 'Graph'
        db.delete_table('graphs_graph')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'graphs.color': {
            'Meta': {'object_name': 'Color'},
            'color': ('colorful.fields.RGBColorField', [], {'max_length': '7'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'graphs.colorpalette': {
            'Meta': {'object_name': 'ColorPalette'},
            'colors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['graphs.Color']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'graphs.graph': {
            'Meta': {'object_name': 'Graph'},
            'graph_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kpi': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graphs.KPI']"}),
            'palette': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graphs.ColorPalette']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'graphs.kpi': {
            'Meta': {'object_name': 'KPI'},
            'granularity': ('django.db.models.fields.IntegerField', [], {'default': '60'}),
            'history': ('django.db.models.fields.IntegerField', [], {'default': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'values': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['graphs.KPIValue']"})
        },
        'graphs.kpivalue': {
            'Meta': {'object_name': 'KPIValue'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        }
    }

    complete_apps = ['graphs']