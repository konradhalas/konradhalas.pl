# Generated by Django 2.0.2 on 2018-02-10 17:00

from django.db import migrations, models
import utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=256)),
                ('sub_title', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(upload_to=utils.models.SlugifyUploadTo(fields=['title'], path='articles'))),
                ('content', models.TextField()),
                ('publish_date', models.DateField()),
                ('update_date', models.DateField()),
                ('is_public', models.BooleanField()),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
