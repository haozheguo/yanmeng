from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userInfo", "0002_alter_customuser_options_customuser_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="avatar",
            field=models.CharField(
                blank=True,
                default="/media/avator/defaultavator.svg",
                max_length=255,
                verbose_name="头像",
            ),
        ),
    ]
