# Generated by Django 4.1.5 on 2023-06-26 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adv_Fname', models.CharField(max_length=255)),
                ('Adv_Lname', models.CharField(max_length=255)),
                ('Username', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Advisor',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Coll_Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cmj_name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Coll_Majors',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'College',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Cur_Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CG_Name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Cur_Group',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fac_Name', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'Faculty',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('G_Name', models.CharField(max_length=200, unique=True)),
                ('Fac_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Faculty', to='Webtranfer.faculty')),
            ],
            options={
                'db_table': 'Groups',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mj_Name', models.CharField(max_length=200, unique=True)),
                ('Fac_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.faculty')),
            ],
            options={
                'db_table': 'Major',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'User',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Useradmin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adm_Fname', models.CharField(max_length=255)),
                ('Adm_Lname', models.CharField(max_length=255)),
                ('Username', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'db_table': 'Admin',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('Std_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Std_Fname', models.CharField(max_length=255)),
                ('Std_Lname', models.CharField(max_length=255)),
                ('Adv_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.advisor')),
                ('Cmj_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.coll_major')),
                ('G_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.groups')),
                ('Mj_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.major')),
                ('Stdusername', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.user')),
            ],
            options={
                'db_table': 'Student',
                'ordering': ('Std_ID',),
            },
        ),
        migrations.AddField(
            model_name='groups',
            name='Mj_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Major', to='Webtranfer.major'),
        ),
        migrations.CreateModel(
            name='Cur_Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ac_Year', models.DateField(verbose_name='')),
                ('Version', models.CharField(max_length=255)),
                ('Cr_total', models.IntegerField(verbose_name='')),
                ('Cr_Man', models.IntegerField(verbose_name='')),
                ('Cr_Math', models.IntegerField(verbose_name='')),
                ('Cr_Lang', models.IntegerField(verbose_name='')),
                ('Cr_Core', models.IntegerField(verbose_name='')),
                ('Cr_Basic', models.IntegerField(verbose_name='')),
                ('Cr_Main', models.IntegerField(verbose_name='')),
                ('Cr_Select', models.IntegerField(verbose_name='')),
                ('Cr_Free', models.IntegerField(verbose_name='')),
                ('Mj_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.major')),
            ],
            options={
                'db_table': 'Cur_Head',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Cur_Detail',
            fields=[
                ('Subj_ID', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('Subj_Cr', models.IntegerField(verbose_name='')),
                ('CG_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.cur_group')),
                ('Cur_Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.cur_head')),
            ],
            options={
                'ordering': ('Subj_ID',),
            },
        ),
        migrations.AddField(
            model_name='coll_major',
            name='Coll_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.college'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='Fac_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.faculty'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='Mj_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Webtranfer.major'),
        ),
        migrations.AlterUniqueTogether(
            name='coll_major',
            unique_together={('Cmj_name', 'Coll_name')},
        ),
    ]
