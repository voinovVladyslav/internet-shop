# Generated by Django 3.2.15 on 2022-12-11 13:54

from django.db import migrations


def create_entries(apps, schema_editor):
    Category = apps.get_model('core', 'Category')
    Item = apps.get_model('core', 'Item')
    alcohol = Category.objects.create(
        name='Alcohol',
        image='alcohol.png',
    )
    acceesories = Category.objects.create(
        name='Accessories',
        image='accessories.png',
    )
    clothes = Category.objects.create(
        name='Clothes',
        image='clothes.png',
    )
    food = Category.objects.create(
        name='Food',
        image='food.png',
    )
    for_baby = Category.objects.create(
        name='For baby',
        image='for-baby.png',
    )
    pets = Category.objects.create(
        name='Pets',
        image='pets.png',
    )
    tools = Category.objects.create(
        name='Tools',
        image='tools.png',
    )
    hardware = Category.objects.create(
        name='Hardware',
        image='pc.png',
    )

    Item.objects.create(
        name='Apple',
        description='Green, yellow or even red, we have all sorts of apples.',
        price='2.9',
        image='apple.png',
    )

    Item.objects.create(
        name='Bones',
        description='Rubber bones for your belowed dog or even child?',
        price='15.66',
        image='bones.png',
    )

    Item.objects.create(
        name='Champagne',
        description='Sparkling water in fonderfuly shaped glass bottle',
        price='17.33',
        image='champagne.png',
    )

    Item.objects.create(
        name='Child bottle',
        description='Anti spill bottle for your little demon',
        price='23.11',
        image='child_bottle.png',
    )

    Item.objects.create(
        name='AMD Ryzen 5 5500',
        description='AM4 socket based CPU from AMD',
        price='123.11',
        image='cpu.png',
    )

    Item.objects.create(
        name='DTEK Jacket',
        description='This jacket is exactly the same as of DTEK electicians, \
so it will provide you uninterrupted electricity all around you',
        price='89.11',
        image='dtekjacket.png',
    )
    
    Item.objects.create(
        name='Hammer',
        description='Steel head and wooden handle, overall weight approximately 8 kg.',
        price='50.11',
        image='hammer.png',
    )
    
    Item.objects.create(
        name='Hat',
        description='Once man bought a hat and it was just right for him',
        price='35.21',
        image='hat.png',
    )
    
    Item.objects.create(
        name='Lobster',
        description='Red lobster right from our local puddle',
        price='90.11',
        image='lobster.png',
    )
    
    Item.objects.create(
        name='Watermelon',
        description='The most tastier watermelons, right from Kherson fields',
        price='0.80',
        image='watermelon.png',
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_item'),
    ]

    operations = [
        migrations.RunPython(
            code=create_entries,
            reverse_code=migrations.RunPython.noop,
        )
    ]