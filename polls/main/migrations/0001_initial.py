# Generated by Django 3.2.6 on 2021-08-18 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название модели')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('end_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата окончания')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст вопроса')),
                ('type_of_answer', models.IntegerField(choices=[(0, 'текст'), (1, 'один вариант'), (2, 'множество вариантов')], verbose_name='Тип вопроса')),
                ('answer', models.JSONField(default=dict, verbose_name='Ответ')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.poll', verbose_name='Опрос')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]