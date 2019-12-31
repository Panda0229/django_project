from django.db import models

# Create your models here.


class AreaInfo(models.Model):
    '''地址模型类'''
    # 地区名称                    指定列的标题
    atitle = models.CharField(verbose_name='标题', max_length=20)
    # 自关联属性
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    # 更改显示的名称
    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle
    # 点击根据atitle进行排序
    title.admin_order_field = 'atitle'
    # 设置title的名称
    title.short_description = '地区名称'

    def parent(self):
        if self.aParent is None:
            return ''
        return self.aParent.atitle
    # 设置parent的列名
    parent.short_description = '父级地区名称'


class PicTest(models.Model):
    '''上传图片'''
    goods_pic = models.ImageField(upload_to='booktest')  # upload指定上传的目录，这个目录是根据media定位的

