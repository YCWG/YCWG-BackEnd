# Generated by Django 4.1.7 on 2023-06-09 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party_list', '0003_remove_party_image_alter_party_member_limit_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='party',
            name='date',
            field=models.CharField(max_length=28, null=True),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
