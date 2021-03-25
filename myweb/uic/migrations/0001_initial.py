# Generated by Django 3.1.7 on 2021-03-06 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('cname', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'uic_courses',
            },
        ),
        migrations.CreateModel(
            name='Course_Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uic.course')),
            ],
            options={
                'db_table': 'course_teacher',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=20)),
                ('emailAdd', models.EmailField(default='2161217535@qq.com', max_length=254)),
                ('course', models.ManyToManyField(through='uic.Course_Teacher', to='uic.Course')),
            ],
            options={
                'db_table': 'uic_teachers',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(blank=True, max_length=20, null=True)),
                ('password', models.CharField(blank=True, max_length=20, null=True)),
                ('register_time', models.DateTimeField(blank=True, null=True)),
                ('image', models.ImageField(null=True, upload_to='student_image')),
                ('emailAdd', models.EmailField(default='2161217535@qq.com', max_length=254)),
                ('course_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uic.course')),
            ],
            options={
                'db_table': 'uic_students',
            },
        ),
        migrations.AddField(
            model_name='course_teacher',
            name='tid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uic.teacher'),
        ),
    ]
