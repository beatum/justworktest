# Generated by Django 2.1.7 on 2019-04-01 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basetype', '0004_auto_20190331_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagebasetype',
            name='audio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='basetype_pagebasetype_related', to='basetype.AudioBaseType'),
        ),
        migrations.AlterField(
            model_name='pagebasetype',
            name='text',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='basetype_pagebasetype_related', to='basetype.TextBaseType'),
        ),
        migrations.AlterField(
            model_name='pagebasetype',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='basetype_pagebasetype_related', to='basetype.VideoBaseType'),
        ),
    ]