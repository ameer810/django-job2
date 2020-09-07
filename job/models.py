from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import django_filters
from django_countries.fields import CountryField

# Create your models here.


JOB_TYPE = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)


def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s" % (instance.id, extension)


class Job(models.Model):
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    location = CountryField()
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    emails = models.EmailField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload, blank=True, null=True)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('jobs:job_detail', args=[str(self.id)])

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Apply(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/', blank=True, null=True)
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Apply, self).save(*args, **kwargs)

    def __str__(self):
        return self.name





































'''
السلام عليكم كابتن
بس اريد احجي وياك بموضوع
كابتن انا اخر 5 لعبات لعبت بس 3 دقايق
ف اريد اعرف شلون انت تعرف وتقيم مستوايه اذا انا لاعب بس 3 دقايق اخر 5 لعبات؟؟
اذا تقيمو بالتمارين الي ناخذها ف انا كل التمارين دا اسويه بس كم تمرين ما اقدرله
قصدي ع تمارين القوة واللياقة
انا مو علمود اريد العب وهاهيه. ومدا اكول انا خوش لاعب
 انا اريدك تنطيني فرصة تشوف بيها مستوايه زين لا ؟


كابتن انا احس محد مهتم بيه لا بالتمرين ولا بالعبة
مثلا ولا مرة بالتمرين احد كايلي هاي غلط , هاي صح
عكس بقية اللواعيب توكف ع راسهم بس تريدهم يطبقون تشجعهم تحجي وياهم تكلهم هاي خطأ تصححلهم بينما انا محد دايرلي بال
ليش شنو فرقهم عني
حتى باللعبات من تلعبني اخر شي متباوع ولا تنتبه عليه يمكن انت تقول خطيه امير ملعبتها خل العبها يعني انت مرايدني لان محتاجني باللعبة مثلا. بس علمود العب ومن العب ماكو لا تكلي لعبت زين ولا تكلي لعب مو زين انا هاي اريدك اتكلياها
انا هاي مهامتني وعادي عندي بس داشوفك الفرق بيني وبينهم

يعني انا اريد من العب تكلي شنو اخطائي تكلي عندك هيج شي طوره
"مثل البقية"
هاي اذا انطيتني فرصة العب
انطيني فرصة وشوفني يمكن العب اسوء لعب ويمكن العب خوش لعب
كابتن انا من ارجع للبيت اكول ليش الكابتن مدخلني باللعبة شنو الي شافو عني ومخلاه يلعبنيي؟؟
كلي علمود افتهم واشتغل عليه
وارجع واكول انا ماهمني اللعب انا هامني انو انت تشوف مستوايه وتكلي اخطائي وين و(تهتم بيه مثل البقيه)
انا هذا الحجي صارلي فترة اريد احجيه بس مستحي منك
واسف اذا تجاوزت حدودي او حجيت شي خطأ
'''