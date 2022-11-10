# Generated by Django 4.1.3 on 2022-11-09 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_coms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=360)),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=360)),
                ('com_com', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.comment_coms')),
                ('like', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.likes')),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.comments')),
                ('like', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.likes')),
            ],
        ),
    ]
