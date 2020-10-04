from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):  #over write
        return self.question_text

class Choice(models.Model):
    '''
    Ngoài các kiểu dữ liệu thường dùng thì chúng ta còn có kiểu khóa ngoại
    được định nghĩa trong lớp ForeignKey, tham số đầu tiên là bảng mà khóa
    ngoại này tham chiếu tới, on_delete=models.CASCADE tức là khi dữ liệu
    trong bảng cha có sự thay đổi thì dữ liệu trong bảng con cũng sẽ thay
    đổi theo, chẳng hạn như bản ghi trong bảng Question bị xóa thì các
    bản ghi trong bảng Choice có tham chiếu tới bản ghi trong bảng Question
    này cũng sẽ bị xóa.
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



