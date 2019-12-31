from django.db import models

# Create your models here.


# 一类
# 图书类
class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称，CharField说明是一个字符串，max_length制定字符串最大的长度
    btitle = models.CharField(max_length=20)
    # 出版日期，DataField说明是一个日期类型
    bpub_date = models.DateField()

    def __str__(self):
        # 返回书名
        return self.btitle


# 多类
# 人物类 名字，性别，年龄，备注
# 关系属性：建立图书类和人物类的一对多关系 hbook
class HeroInfo(models.Model):
    """人物模型类"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    # 关系属性，建立图书类和人物类之间一对多的关系
    # 关系属性对应的表的字段名格式：关系属性名_id
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname
