from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from slugify import slugify
from django.utils import timezone


class GamePost(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Проект'),
        ('published', 'Изданный'),
    ]
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Статья')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Время публикации')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Статус")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор")
    tags = models.ManyToManyField('TagArticle', blank=True, related_name='tags')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Статьи о играх'
        verbose_name_plural = 'Статьи о играх'
        ordering = ['-time_create', 'title', '-publish']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категории игр'
        verbose_name_plural = 'Категории игр'


class Comment(models.Model):
    article_id = models.ForeignKey(GamePost, on_delete=models.CASCADE, verbose_name='Статья')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    email = models.EmailField(verbose_name='e-mail')
    content = models.TextField(blank=True, verbose_name='Комментарий')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото')
    photo1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото1')
    photo2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name='Фото2')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время редактирования')
    active = models.BooleanField(default=True, verbose_name='Опубликовать?')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарий'
        ordering = ('created',)

    def __str__(self):
        return 'Комментарий от {} для {}'.format(self.author_id, self.article_id)


class TagArticle(models.Model):
    tag = models. CharField(max_length=100, db_index=True)
    slug = models. SlugField(max_length=255, unique=True, db_index=True)

    def __str__ (self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})