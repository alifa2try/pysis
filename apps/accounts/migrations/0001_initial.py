# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Course'
        db.create_table('accounts_course', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('level', self.gf('django.db.models.fields.CharField')(default='UG', max_length=4)),
        ))
        db.send_create_signal('accounts', ['Course'])

        # Adding model 'Batch'
        db.create_table('accounts_batch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=5)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Course'], null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
        ))
        db.send_create_signal('accounts', ['Batch'])

        # Adding model 'Profile'
        db.create_table('accounts_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], unique=True)),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Course'], null=True, blank=True)),
            ('year_of_joining', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=0, blank=True)),
            ('college_email_id', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=2)),
            ('blood_group', self.gf('django.db.models.fields.CharField')(max_length=4, null=True, blank=True)),
            ('date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('actual_date_of_birth', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('father_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('father_profession', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('family_income', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('religion', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('caste', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('reservation_category', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('personal_email_id', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('personal_email_id2', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('personal_contact_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('personal_contact_number2', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('emergency_contact_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('present_address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('permanent_address', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('sslc_passed_out_year', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=0, blank=True)),
            ('sslc_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('hslc_passed_out_year', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=0, blank=True)),
            ('hslc_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('hslc_major', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('ug_passed_out_year', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=0, blank=True)),
            ('ug_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('ug_major', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('pg_passed_out_year', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=0, blank=True)),
            ('pg_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=4, decimal_places=2, blank=True)),
            ('pg_major', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('history_of_arrears', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('nss', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('ncc', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('sports', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('hobbies', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('personal_website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('orkut_profile_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('facebook_profile_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('linkedin_profile_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('google_account_created', self.gf('django.db.models.fields.BooleanField')(default=False, blank=True)),
            ('last_modified_on', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal('accounts', ['Profile'])


    def backwards(self, orm):
        
        # Deleting model 'Course'
        db.delete_table('accounts_course')

        # Deleting model 'Batch'
        db.delete_table('accounts_batch')

        # Deleting model 'Profile'
        db.delete_table('accounts_profile')


    models = {
        'accounts.batch': {
            'Meta': {'object_name': 'Batch'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Course']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'accounts.course': {
            'Meta': {'object_name': 'Course'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'default': "'UG'", 'max_length': '4'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        'accounts.profile': {
            'Meta': {'object_name': 'Profile'},
            'actual_date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'blood_group': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'caste': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'college_email_id': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Course']", 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'emergency_contact_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'facebook_profile_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'family_income': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'father_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'father_profession': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '2'}),
            'google_account_created': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'history_of_arrears': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'hobbies': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'hslc_major': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'hslc_passed_out_year': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '0', 'blank': 'True'}),
            'hslc_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'linkedin_profile_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ncc': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'nss': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'orkut_profile_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'permanent_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'personal_contact_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'personal_contact_number2': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'personal_email_id': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'personal_email_id2': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'personal_website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pg_major': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'pg_passed_out_year': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '0', 'blank': 'True'}),
            'pg_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'present_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'religion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'reservation_category': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'sports': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'sslc_passed_out_year': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '0', 'blank': 'True'}),
            'sslc_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'ug_major': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'ug_passed_out_year': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '0', 'blank': 'True'}),
            'ug_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '2', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'year_of_joining': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '0', 'blank': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['accounts']
