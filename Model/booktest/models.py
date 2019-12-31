from django.db import models


# Create your models here.
# 重写管理器类
class BookInfoManager(models.Manager):
    """图书模型管理器类"""
    # 作用1 ：重写查询的结果，使查询到的值为isdelte=Flase的值
    def all(self):
        # 使用父类的all()方法来查询所有值
        books = super().all()
        # 使用all所查询到的值为Queryset对象，可以链式调用，对其进行筛选
        books = books.filter(isDelete=False)
        # 返回过滤之后的结果
        return books

    # 作用2：封装函数：操作模型类对应的数据表(增删改查)
    def create_book(self, btitle, bpub_date):
        # 创建一个图书对象
        # 获取self所在的模型类
        model_class = self.model
        book = model_class()
        # book = BookInfo()
        book.btitle = btitle
        book.bpub_date = bpub_date
        # 保存对象
        book.save()
        # 返回对象
        return book


# 一类
# 模型类自动生成的表名是应用名_模型类名
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.CharField(max_length=200, default=0)
    isDelete = models.BooleanField(default=False)

    # 查询所用的objects是一个管理器对象，自己定义了一个管理器对象后，原来的objects便不可以使用
    # book = models.Manager()  # 自定义一个Manager
    objects = BookInfoManager()  # 创建一个管理器对象，与开始默认的objects不同

    # 防止更改应用名时表名变化产生的一系列错误
    class Meta:
        db_table = 'bookinfo'  # 指定模型类对应的表名


# 多类
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)
    isDelete = models.BooleanField(default=False)

'''
class NewsType(models.Model):
    """类型名"""
    # 类型名
    type_name = models.CharField(max_length=20)
    # 关系属性
    # 多对多关系在哪个类中建立都可以
    type_news = models.ManyToManyField('News')
    
    
class News(models.Model):
    """新闻类"""
    # 新闻标题
    title = models.CharField(max_length=20)
    # 发布时间
    pub_date = models.DateTimeField(auto_now_add=True)
    # 信息内容
    content = models.TextField()
    # 关系属性
    # news_type = models.ManyToManyField('NewsType')
    
    
class EmployeeBasicInfo(models.Model):
    """员工基本信息"""
    # 姓名
    name = models.CharField(max_length=20)
    # 性别
    gender = models.BooleanField(default=False)
    # 年龄
    age = models.IntegerField()
    # 关系属性，代表员工的详细信息
    employee_detail = models.OneToOneField('EmployeeDetailInfo')
    
    
class EmployeeDetailInfo(models.Model):
    """员工详细信息"""
    # 联系地址
    addr = models.CharField(max_length=256)
    # 关系属性,代表员工的基本信息
    employee_basic = models.OneToOneField('EmployeeBasicInfo')  
'''


class AreaInfo(models.Model):
    """地区模型类"""
    # 地区名称
    atitle = models.CharField(max_length=20)
    # 建立关系属性（自相关）,代表当前地区的父级地区
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)












