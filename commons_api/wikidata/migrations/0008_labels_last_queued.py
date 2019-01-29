# Generated by Django 2.1.5 on 2019-01-29 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wikidata', '0007_add_boundary_foreignkeys'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrativearea',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='election',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='electoraldistrict',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legislativehouse',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='legislativeterm',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='position',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='term',
            name='refresh_labels_last_queued',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]