# Generated by Django 3.2.11 on 2022-02-22 04:21

import _socket
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.models.validators.date
import edc_sites.models
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LpCsf',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=50, unique=True)),
                ('bios_crag', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text='Gaborone and Blantyre only', max_length=5, verbose_name='Biosynex Semi-quantitative CrAg performed?')),
                ('crag_control_result', models.CharField(choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('N/A', 'Not applicable')], default='N/A', help_text='Gaborone and Blantyre only', max_length=5, verbose_name='Control result')),
                ('crag_t1_result', models.CharField(choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('N/A', 'Not applicable')], default='N/A', help_text='Gaborone and Blantyre only', max_length=5, verbose_name='T1 result')),
                ('crag_t2_result', models.CharField(choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('N/A', 'Not applicable')], default='N/A', help_text='Gaborone and Blantyre only', max_length=5, verbose_name='T2 result')),
                ('csf_assay_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='CSF Result Report Date and Time')),
                ('csf_culture', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('awaiting_results', 'Awaiting results'), ('not_done', 'Not done')], default='awaiting_results', help_text='Complete after getting the results.', max_length=18, verbose_name='Other organism (non-Cryptococcus)')),
                ('other_csf_culture', models.CharField(blank=True, max_length=75, null=True, verbose_name='If YES, specify organism:')),
                ('csf_wbc_cell_count', models.IntegerField(blank=True, help_text='acceptable units are mm<sup>3</sup>', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total CSF WBC cell count:')),
                ('differential_lymphocyte_count', models.IntegerField(blank=True, help_text='acceptable units are mm<sup>3</sup> or %', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Differential lymphocyte cell count:')),
                ('differential_lymphocyte_unit', models.CharField(blank=True, choices=[('mm3', 'mm<sup>3</sup>'), ('%', '%')], max_length=6, null=True)),
                ('differential_neutrophil_count', models.IntegerField(blank=True, help_text='acceptable units are mm<sup>3</sup> or %', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Differential neutrophil cell count:')),
                ('differential_neutrophil_unit', models.CharField(blank=True, choices=[('mm3', 'mm<sup>3</sup>'), ('%', '%')], max_length=6, null=True)),
                ('india_ink', models.CharField(blank=True, choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('IND', 'Indeterminate')], max_length=15, null=True)),
                ('csf_glucose', models.DecimalField(blank=True, decimal_places=1, help_text='Units in mmol/L or mg/dL', max_digits=3, null=True, verbose_name='CSF glucose:')),
                ('csf_glucose_units', models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=6, null=True, verbose_name='CSF glucose units:')),
                ('csf_protein', models.DecimalField(blank=True, decimal_places=2, help_text='Units in g/L', max_digits=4, null=True, verbose_name='CSF protein:')),
                ('csf_cr_ag', models.CharField(blank=True, choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('IND', 'Indeterminate')], max_length=15, null=True, verbose_name='CSF CrAg:')),
                ('csf_cr_ag_lfa', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='CSF CrAg done by IMMY CrAg LFA:')),
                ('qc_assay_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='QC Result Report Date and Time')),
                ('quantitative_culture', models.IntegerField(blank=True, help_text='Units CFU/ml', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)])),
                ('lp_datetime', models.DateTimeField(validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='LP Date and Time')),
                ('reason_for_lp', models.CharField(choices=[('scheduled_per_protocol', 'Scheduled per protocol'), ('therapeutic_lp', 'Therapeutic LP'), ('clincal_deterioration', 'Clinical deterioration')], max_length=50, verbose_name='Reason for LP')),
                ('opening_pressure', models.IntegerField(help_text='Units cm of H<sub>2</sub>O', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('closing_pressure', models.IntegerField(blank=True, help_text='Units cm of H<sub>2</sub>O', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('csf_amount_removed', models.IntegerField(blank=True, help_text='Units ml', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='CSF amount removed ')),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow)),
                ('site', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'Lumbar Puncture/Cerebrospinal Fluid',
                'verbose_name_plural': 'Lumbar Puncture/Cerebrospinal Fluid',
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
                'abstract': False,
                'default_permissions': ('add', 'change', 'delete', 'view', 'export', 'import'),
            },
            managers=[
                ('on_site', edc_sites.models.CurrentSiteManager()),
                ('objects', edc_visit_tracking.managers.CrfModelManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalLpCsf',
            fields=[
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('created', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('modified', models.DateTimeField(blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow)),
                ('user_created', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user created')),
                ('user_modified', django_audit_fields.fields.userfield.UserField(blank=True, help_text='Updated by admin.save_model', max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(blank=True, default=_socket.gethostname, help_text='System field. (modified on create only)', max_length=60)),
                ('hostname_modified', django_audit_fields.fields.hostname_modification_field.HostnameModificationField(blank=True, help_text='System field. (modified on every save)', max_length=50)),
                ('device_created', models.CharField(blank=True, max_length=10)),
                ('device_modified', models.CharField(blank=True, max_length=10)),
                ('id', django_audit_fields.fields.uuid_auto_field.UUIDAutoField(blank=True, db_index=True, editable=False, help_text='System auto field. UUID primary key.')),
                ('subject_identifier', models.CharField(db_index=True, max_length=50)),
                ('bios_crag', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', help_text='Gaborone and Blantyre only', max_length=5, verbose_name='Biosynex Semi-quantitative CrAg performed?')),
                ('crag_control_result', models.CharField(choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('N/A', 'Not applicable')], default='N/A', help_text='Gaborone and Blantyre only', max_length=5, verbose_name='Control result')),
                ('crag_t1_result', models.CharField(choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('N/A', 'Not applicable')], default='N/A', help_text='Gaborone and Blantyre only', max_length=5, verbose_name='T1 result')),
                ('crag_t2_result', models.CharField(choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('N/A', 'Not applicable')], default='N/A', help_text='Gaborone and Blantyre only', max_length=5, verbose_name='T2 result')),
                ('csf_assay_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='CSF Result Report Date and Time')),
                ('csf_culture', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('awaiting_results', 'Awaiting results'), ('not_done', 'Not done')], default='awaiting_results', help_text='Complete after getting the results.', max_length=18, verbose_name='Other organism (non-Cryptococcus)')),
                ('other_csf_culture', models.CharField(blank=True, max_length=75, null=True, verbose_name='If YES, specify organism:')),
                ('csf_wbc_cell_count', models.IntegerField(blank=True, help_text='acceptable units are mm<sup>3</sup>', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Total CSF WBC cell count:')),
                ('differential_lymphocyte_count', models.IntegerField(blank=True, help_text='acceptable units are mm<sup>3</sup> or %', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Differential lymphocyte cell count:')),
                ('differential_lymphocyte_unit', models.CharField(blank=True, choices=[('mm3', 'mm<sup>3</sup>'), ('%', '%')], max_length=6, null=True)),
                ('differential_neutrophil_count', models.IntegerField(blank=True, help_text='acceptable units are mm<sup>3</sup> or %', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Differential neutrophil cell count:')),
                ('differential_neutrophil_unit', models.CharField(blank=True, choices=[('mm3', 'mm<sup>3</sup>'), ('%', '%')], max_length=6, null=True)),
                ('india_ink', models.CharField(blank=True, choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('IND', 'Indeterminate')], max_length=15, null=True)),
                ('csf_glucose', models.DecimalField(blank=True, decimal_places=1, help_text='Units in mmol/L or mg/dL', max_digits=3, null=True, verbose_name='CSF glucose:')),
                ('csf_glucose_units', models.CharField(blank=True, choices=[('mg/dL', 'mg/dL'), ('mmol/L', 'mmol/L (millimoles/L)')], max_length=6, null=True, verbose_name='CSF glucose units:')),
                ('csf_protein', models.DecimalField(blank=True, decimal_places=2, help_text='Units in g/L', max_digits=4, null=True, verbose_name='CSF protein:')),
                ('csf_cr_ag', models.CharField(blank=True, choices=[('POS', 'Positive'), ('NEG', 'Negative'), ('IND', 'Indeterminate')], max_length=15, null=True, verbose_name='CSF CrAg:')),
                ('csf_cr_ag_lfa', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('N/A', 'Not applicable')], default='N/A', max_length=5, verbose_name='CSF CrAg done by IMMY CrAg LFA:')),
                ('qc_assay_datetime', models.DateTimeField(blank=True, null=True, validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='QC Result Report Date and Time')),
                ('quantitative_culture', models.IntegerField(blank=True, help_text='Units CFU/ml', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100000000)])),
                ('lp_datetime', models.DateTimeField(validators=[edc_model.models.validators.date.datetime_not_future], verbose_name='LP Date and Time')),
                ('reason_for_lp', models.CharField(choices=[('scheduled_per_protocol', 'Scheduled per protocol'), ('therapeutic_lp', 'Therapeutic LP'), ('clincal_deterioration', 'Clinical deterioration')], max_length=50, verbose_name='Reason for LP')),
                ('opening_pressure', models.IntegerField(help_text='Units cm of H<sub>2</sub>O', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(99)])),
                ('closing_pressure', models.IntegerField(blank=True, help_text='Units cm of H<sub>2</sub>O', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(99)])),
                ('csf_amount_removed', models.IntegerField(blank=True, help_text='Units ml', null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='CSF amount removed ')),
                ('report_datetime', models.DateTimeField(default=edc_utils.date.get_utcnow)),
                ('history_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('site', models.ForeignKey(blank=True, db_constraint=False, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='sites.site')),
            ],
            options={
                'verbose_name': 'historical Lumbar Puncture/Cerebrospinal Fluid',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
