# Generated by Django 3.2.13 on 2024-08-15 04:26

import base.models.item_models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(default=base.models.item_models.create_id, max_length=50, primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, default='名無し', max_length=50, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('slug', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('slug', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.CharField(default=base.models.item_models.create_id, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('uid', models.CharField(editable=False, max_length=50, verbose_name='user紐付け')),
                ('title', models.CharField(max_length=50, verbose_name='タイトル')),
                ('text', models.TextField(verbose_name='詳細文')),
                ('thumbnail', models.ImageField(blank=True, default='', upload_to=base.models.item_models.upload_image_to, verbose_name='画像')),
                ('movie', models.FileField(blank=True, null=True, upload_to=base.models.item_models.upload_movie_to, verbose_name='動画')),
                ('is_published', models.BooleanField(default=True, verbose_name='公開設定')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category')),
                ('tags', models.ManyToManyField(blank=True, to='base.Tag')),
            ],
        ),
    ]
