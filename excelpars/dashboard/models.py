from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
import uuid


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return '{}/{}'.format(instance.slug, filename)


def create_object_info_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        slug = slugify(translit(instance.nativeName, reversed=True))
        instance.slug = slug + '-'+uuid.uuid4().hex
        print(instance.slug)


class ObjectInfo(models.Model):

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    slug = models.SlugField(
        verbose_name='slugURL',
        max_length=400,
        null=True,
        blank=True
    )

    id_openData = models.CharField(
        max_length=200, 
        verbose_name='ID opendata.mkrf.ru',
        blank=True,
        null=True)

    nativeName = models.CharField(
        max_length=200,
        verbose_name='Наименование',
        blank=True,
        null=True
    )
    fullAddress = models.TextField(
        verbose_name='Полный адрес',
        blank=True,
        null=True
    )
    municipality = models.ForeignKey(
        'Municipality', 
        on_delete=models.CASCADE, 
        verbose_name='Муниципальное образование',
        blank=True,
        null=True
    )
    locality = models.ForeignKey(
        'Locality', 
        on_delete=models.CASCADE, 
        verbose_name='Населенный пункт',
        blank=True,
        null=True
    )
    
    YES = 'Yes'
    NO = 'No'
    IN_WORK = 'In_work'
    information_CHOICES = (
        (YES, 'Да'),
        (NO, 'Нет'), 
        (IN_WORK, 'На подготовке')
    )
    like_BOOLEAN = (
        (YES, 'Да'),
        (NO,  'Нет'),
    )

    OKN_in_ensemble = models.CharField(
        verbose_name='ОКН входит в ансамбль (да/нет)',
        choices=like_BOOLEAN,
        blank=True,
        null=True,
        max_length=10
     
    )
  

    information_sign = models.CharField(
        choices=information_CHOICES, 
        max_length=5,
        verbose_name='Наличие уcтановленной информационной надписи установленного образца',
        blank=True,
        null=True
    ) 
    information_sign_photo = models.ImageField(
        upload_to=image_folder, 
        blank=True,
        null=True,
        verbose_name='Фотография информационной надписи',
    )
    information_sign_conformity = models.CharField(
        verbose_name='Наличие информационной надписи, но не соответствующей требованиям',
        blank=True,
        null=True,
        choices=like_BOOLEAN,
        max_length=10

        
    )
    photo = models.ImageField(
        upload_to=image_folder, 
        blank=True,
        verbose_name='Фото',
        null=True

    )
    url = models.CharField(
        max_length=200,
        verbose_name='URL адрес',
        blank=True,
        null=True
        
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    affiliation_U = models.CharField(
        choices=like_BOOLEAN,
        verbose_name='Принадлежность к ЮНЭСКО',
        blank=True,
        null=True,
        max_length=10
        
    )
    esp_valuable_object = models.CharField(
        choices=like_BOOLEAN,
        verbose_name='Особо ценный объект',
        blank=True,
        null=True,
        max_length=10
        
    )
    requisites_and_title = models.TextField(
        verbose_name=' Реквизиты и наименование акта органа государственной власти о постановке на государственную охрану объекта культурного наследия',
        blank=True,
        null=True
    )
    owner = models.CharField(
        max_length=200,
        verbose_name='Собственник',
        blank=True,
        null=True
    )
    management = models.CharField(
        max_length=200,
        verbose_name='Под чьим управлением',
        blank=True,
        null=True
    )
    owner_contacts = models.TextField(
        verbose_name='Контактные данные собственника ОКН',
        blank=True,
        null=True
    )
    has_security_obligation = models.CharField(
        choices=information_CHOICES, 
        max_length=5,
        verbose_name='Наличие охранного обязательства ОКН',
        blank=True,
        null=True
    )
    has_passport_OKN = models.CharField(
        choices=information_CHOICES, 
        max_length=5,
        verbose_name='Наличие паспорта ОКН',
        blank=True,
        null=True
    )
    actual_address = models.TextField(
        verbose_name='Актуальный адрес',
        blank=True,
        null=True
    )
    gen_species_appearance = models.ForeignKey(
        'Species', 
        on_delete=models.CASCADE,
        verbose_name='Общая видовая принадлежность',
        blank=True,
        null=True
    )
    has_docs_boundaries = models.CharField(
        choices=like_BOOLEAN,
        verbose_name='Наличие документов о границах территории ОКН',
        blank=True,
        null=True,
        max_length=10
    )
    req_of_approval = models.TextField(
        verbose_name='Реквизиты об утверждении границ территории',
        blank=True,
        null=True
        
    )
    has_docs_of_aprroval = models.CharField(
        verbose_name='Наличие документов об утвержденых зонах охраны',
        blank=True,
        null=True,
        max_length=10,
        choices=like_BOOLEAN
    )
    document_on_approved_security = models.TextField(
        verbose_name='Документ об утвержденых зонах охраны',
        blank=True,
        null=True
    )
    has_rights = models.CharField(
        verbose_name='Наличие зарегистрированных прав/обременений',
        blank=True,
        null=True,
        max_length=10,
        choices=like_BOOLEAN
    )
    date = models.DateField(
        verbose_name='Дата',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nativeName

pre_save.connect(create_object_info_slug, sender=ObjectInfo)





class Municipality(models.Model):
    
    class Meta:
        verbose_name = 'Муниципальное образование'
        verbose_name_plural = 'Муниципальные образования'

    name = models.CharField(
        max_length=200,
        verbose_name='Муниципальное образование'
    )
 
    def __str__(self):
        return self.name



class Locality(models.Model):

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'

    name = models.CharField(
        verbose_name='Населенный пункт',
        max_length=200
    )

    def __str__(self):
        return self.name


class Species(models.Model):

    class Meta:
        verbose_name = 'Видовая принадлежность'
        verbose_name_plural = 'Видовые принадлежности'

    name = models.CharField(
        verbose_name='Общая видовая принадлежность',
        max_length=200
    )
    
    def __str__(self):
        return self.name