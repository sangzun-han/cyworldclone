# Generated by Django 3.0.8 on 2020-07-28 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_diary'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='diary_title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
