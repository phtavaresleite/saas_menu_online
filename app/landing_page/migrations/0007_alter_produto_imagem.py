# Generated by Django 4.2.16 on 2024-10-08 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_page', '0006_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(default='app/media/produtos/placeholder.png', upload_to='produtos/', verbose_name='Foto'),
        ),
    ]
