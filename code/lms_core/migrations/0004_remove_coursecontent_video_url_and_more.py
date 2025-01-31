# Generated by Django 5.1.4 on 2025-01-05 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_core', '0003_coursecontent_coursemember_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursecontent',
            name='video_url',
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nama'),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='coursecontent',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='coursemember',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
