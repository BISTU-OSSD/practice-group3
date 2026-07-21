from django.db import models
from schedule.models import Course

class Grade(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    student_name = models.CharField(max_length=50, verbose_name="学生姓名")
    score = models.FloatField(verbose_name="成绩")
    semester = models.CharField(max_length=20, verbose_name="学期")

    def __str__(self):
        return f"{self.student_name} - {self.course.name}: {self.score}"
