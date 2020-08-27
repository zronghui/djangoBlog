from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Post(models.Model):
    # 标题
    title = models.CharField('标题', max_length=70)
    # 正文
    body = models.TextField('正文')
    # 创建时间 最后修改时间
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('最后修改时间')
    # 摘要
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    # 分类与标签
    # 分类 一篇文章有 1 个分类 category 删除时，对应的所有文章删除
    # 标签 可以有多个标签
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    # 作者
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('myBlog:detail', kwargs={'pk': self.pk})
