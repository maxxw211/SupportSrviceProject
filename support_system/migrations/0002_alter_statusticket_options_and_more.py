# Generated by Django 4.0a1 on 2021-10-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statusticket',
            options={'verbose_name': ' Статус тикета', 'verbose_name_plural': 'Статусы тикетов'},
        ),
        migrations.AlterModelOptions(
            name='supportanswer',
            options={'verbose_name': ' Ответ саппорта', 'verbose_name_plural': ' Ответы саппорта'},
        ),
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-created_at'], 'verbose_name': 'Тикет', 'verbose_name_plural': 'Тикеты'},
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='update_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='content',
            field=models.TextField(verbose_name='Содержание тикета'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(blank=True, max_length=125, verbose_name='Название тикета'),
        ),
    ]
