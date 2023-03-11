from django.core.management.base import BaseCommand, CommandError
from NewsPaper.news.models import Post, Category

class Command(BaseCommand):
    help = 'Удаление новостей из выбранной категории'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add.argument('category', type=str)

    def handle(self, *args, **options):
        answer = input(f'Вы действительно хотите удалить категорию {options["category"]}? yes/no')
        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Отменено'))
        try:
            category = Category.objects.get(name=options['category'])
            Post.objects.filter(category=category).delete()
            self.stdout.write(self.style.SUCCESS(f'Cтатьи в категории {category.name} удалены'))
        except category.DoesNot.Exist:
            self.stdout.write(self.style.ERROR(f'Нет такой категории {}'))
