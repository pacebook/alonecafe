from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from authapp.models import CustomUser as User

from PIL import Image


IMAGE_SIZE = (1536, 1028)

def get_upload_path(instance, filename):
    return timezone.now().strftime("%y-%m-%d/") + "/cafe_" + str(instance.cafe.id) + "_photo/" + filename

class Region(models.Model):
    city = models.CharField('광역시도', max_length=20)

    def __str__(self):
        return self.city

class Cafe(models.Model):
    user = models.ForeignKey(User, related_name='cafes', null=False, blank=False)
    name = models.CharField('이름', max_length=20, blank=False, null=False)
    address = models.CharField('위치', max_length=50, blank=False, null=False)
    intro = models.TextField('소개', blank=False, null=False)
    created = models.DateTimeField('등록일', auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('main:cafe_detail', kwargs={'pk':self.id})

class CafePosition(models.Model):
    cafe = models.OneToOneField('Cafe', related_name='position')
    latitude  = models.CharField('위도', max_length=50, blank=False, null=False)
    longitude = models.CharField('경도', max_length=50, blank=False, null=False)

class CafePhoto(models.Model):
    cafe = models.OneToOneField('Cafe', related_name='photo')
    image = models.ImageField(upload_to=get_upload_path, blank=False, null=False)

    def delete(self, *args, **kwargs):
        try:
            self.image.delete()
        except:
            print("이미 파일이 삭제 됐습니다.")
        super(CafePhoto, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(CafePhoto, self).save(**kwargs)
        image = Image.open(self.image)
        image = image.resize(IMAGE_SIZE, Image.ANTIALIAS)
        image.save(self.image.path)
