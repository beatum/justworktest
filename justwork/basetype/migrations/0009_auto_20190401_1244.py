# Generated by Django 2.1.7 on 2019-04-01 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basetype', '0008_auto_20190401_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiobasetype',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='audio', to='basetype.PageBaseType'),
        ),
    ]