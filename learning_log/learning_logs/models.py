from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习主题"""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
