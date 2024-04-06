# Generated by Django 5.0.4 on 2024-04-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='question_text',
        ),
        migrations.RenameField(
            model_name='test',
            old_name='name',
            new_name='subject_Code',
        ),
        migrations.RemoveField(
            model_name='question',
            name='code',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ques_id',
        ),
        migrations.RemoveField(
            model_name='question',
            name='ques_num',
        ),
        migrations.RemoveField(
            model_name='question',
            name='scored',
        ),
        migrations.RemoveField(
            model_name='test',
            name='subjectCode',
        ),
        migrations.RemoveField(
            model_name='test',
            name='timeDuration',
        ),
        migrations.RemoveField(
            model_name='test',
            name='totalMarks',
        ),
        migrations.AddField(
            model_name='test',
            name='exam_code',
            field=models.CharField(default='123AB', max_length=100),
        ),
        migrations.AddField(
            model_name='test',
            name='total_Marks',
            field=models.IntegerField(default=100),
        ),
    ]
