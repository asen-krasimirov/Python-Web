# Generated by Django 3.1 on 2021-05-31 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_auto_20210531_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('cat', 'cat'), ('dog', 'dog'), ('parrot', 'parrot')], max_length=6),
        ),
    ]
