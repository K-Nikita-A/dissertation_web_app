# Команда import импортирует API migrations.
# Это API Django для создания миграции из django.db, встроенного пакета,
# содержащего классы для работы с базами данных.
# Класс Migration — это класс Python, описывающий операции, выполняемые
# во время миграции баз данных. Этот класс является
# расширением migrations.Migration и содержит два списка:
# dependencies: содержит зависимые миграции.
# operations: содержит операции, которые будут выполняться во время проведения миграции.

from django.db import migrations


def create_data(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    Customer(first_name="Customer 001", last_name="Customer 001", email="customer001@email.com", phone="00000000",
             address="Customer 000 Address", description="Customer 001 description").save()


class Migration(migrations.Migration):
    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_data),
    ]
