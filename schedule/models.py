from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="课程名称")
    teacher = models.CharField(max_length=50, verbose_name="授课教师")
    time = models.CharField(max_length=50, verbose_name="上课时间")
    location = models.CharField(max_length=100, verbose_name="上课地点")
    credit = models.IntegerField(verbose_name="学分")

    def __str__(self):
        return self.name
