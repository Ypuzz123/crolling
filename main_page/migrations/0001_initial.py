# Generated by Django 4.2.6 on 2023-10-23 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weblist',
            fields=[
                ('sitenumber', models.IntegerField(db_column='siteNumber', primary_key=True, serialize=False)),
                ('sitename', models.CharField(db_column='siteName', max_length=20)),
                ('siteurl', models.TextField(db_column='siteURL')),
            ],
            options={
                'db_table': 'weblist',
                'managed': False,
            },
        ),
    ]
