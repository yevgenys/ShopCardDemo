from django.db import migrations


def add_demo_items(apps, schema_editor):
    CardItem = apps.get_model("card", "CardItem")

    CardItem(name="DemoItem1", quantity=100).save()
    CardItem(name="DemoItem2", quantity=50).save()
    CardItem(name="DemoItem3", quantity=10).save()


class Migration(migrations.Migration):
    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_demo_items)
    ]
