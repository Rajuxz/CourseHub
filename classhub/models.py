from django.db import models
from django.utils.html import format_html

#--------------[ Subject Database ]--------------------#
class Subject(models.Model):
    s_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()
    icon = models.CharField(max_length = 50)
    is_paid = models.BooleanField()
    def __str__(self):
        return self.name

    def short_desc(self):
        return self.description[:10]
    


#--------------[ Unit Database ]--------------------#
class Unit(models.Model):
    s_id = models.ForeignKey('Subject',on_delete=models.CASCADE)
    u_id = models.AutoField(primary_key=True)
    uname = models.TextField(max_length=100)
    u_description = models.TextField()
    u_video = models.FileField(upload_to='video/%y',null=False)
    u_image = models.ImageField(upload_to='unit-image/')

    def __str__(self):
        return self.name

    def image_format(self):
        return format_html('<img src="unit-image/{}" style="height:30px;width:30px;border-radius:50%;"/>'.format(self.u_image));

    