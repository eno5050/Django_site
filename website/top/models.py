from django.db import models

# Create your models here.
class TopImage(models.Model):
    
    no = models.IntegerField(default=0, verbose_name="掲載No")
    name = models.CharField(max_length = 62, verbose_name="画像名")
    image = models.ImageField(upload_to = 'images/top_image/', verbose_name ='トップ画像')
    init_image = models.ImageField(upload_to = 'images/top_init_image/', verbose_name ='トップ画像(小)')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    is_deleted = models.BooleanField(default=False, verbose_name="削除フラグ")
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "トップページ用画像"