from django.db import models
import django
from django.utils.safestring import mark_safe

# Create your models here.


class Coser(models.Model):
    u""" Coser 整片文章  """
    # 分类
    title = models.CharField(max_length=255, verbose_name=u"标题", blank=False, default=u'NUll')
    url  = models.TextField(max_length=255, verbose_name=u"图片地址", blank=False, default=u'NUll')
    Rurl = models.TextField(max_length=255, verbose_name=u"图片来源地址", blank=False, default=u'NUll')
    #
    # istop     = models.BooleanField(default=False, verbose_name=u"置顶")
    # come_from = models.CharField(max_length=255, verbose_name=u"来源网站", default=u"Mikufan")
    # topimage  = models.CharField(max_length=255, verbose_name=u"封面图片", default=u"null")
    # addtime   = models.DateTimeField(default=django.utils.timezone.now, blank=True, verbose_name=u"添加时间")

    #
    # def topimage_tag(self):
    #     result = '<img src="%s", width=200px />' % self.topimage
    #     return mark_safe(result)
    #
    # topimage_tag.allow_tags = True
    # topimage_tag.short_description = u"图片预览"