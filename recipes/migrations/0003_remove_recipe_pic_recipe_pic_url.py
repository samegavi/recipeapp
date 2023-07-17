
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='pic',
        ),
        migrations.AddField(
            model_name='recipe',
            name='pic_url',
            field=models.URLField(default='https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg'),
        ),
    ]