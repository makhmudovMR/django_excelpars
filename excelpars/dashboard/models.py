from django.db import models


class ObjectInfo(models.Model):
    id_openData = models.CharField(
        max_length=200,
        verbose_name='ID opendata.mkrf.ru')
    nativeName = models.CharField(
        max_length=200,
        verbose_name='Наименование'
    )
    fullAddress = models.TextField(
        verbose_name='Полный адрес'
    )
    municipality = models.ForeignKey(
        'Municipality',
        on_delete=models.CASCADE,
        verbose_name='Муниципальное образование'
    )
    locality = models.ForeignKey(
        'Locality',
        on_delete=models.CASCADE,
        verbose_name='Населенный пункт'
    )
    OKN_in_ensemble = models.BooleanField(
        verbose_name='ОКН входит в ансамбль (да/нет)'
    )
    YES = 'Yes'
    NO = 'No'
    IN_WORK = 'In_work'
    information_CHOICES = (
        (YES, 'Да'),
        (NO, 'Нет'),
        (IN_WORK, 'На подготовке')
    )
    information_sign = models.CharField(
        choices=information_CHOICES,
        max_length=5,
        verbose_name='Наличие уcтановленной информационной надписи установленного образца'
    )
    information_sign_photo = models.CharField(
        max_length=200,
        verbose_name='Фотография информационной надписи'
    )
    information_sign_conformity = models.BooleanField(
        verbose_name='Наличие информационной надписи, но не соответствующей требованиям'
    )
    photo = models.CharField(
        max_length=200,
        verbose_name='Фото'
    )
    url = models.CharField(
        max_length=200,
        verbose_name='URL адрес'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    affiliation_U = models.BooleanField(
        verbose_name='Принадлежность к ЮНЭСКО'
    )
    esp_valuable_object = models.BooleanField(
        verbose_name='Особо ценный объект'
    )
    requisites_and_title = models.TextField(
        verbose_name=' Реквизиты и наименование акта органа государственной власти о постановке на государственную охрану объекта культурного наследия'
    )
    owner = models.CharField(
        max_length=200,
        verbose_name='Собственник'
    )
    management = models.CharField(
        max_length=200,
        verbose_name='Под чьим управлением'
    )
    owner_contacts = models.TextField(
        verbose_name='Контактные данные собственника ОКН'
    )
    has_security_obligation = models.CharField(
        choices=information_CHOICES,
        max_length=5,
        verbose_name='Наличие охранного обязательства ОКН'
    )
    has_passport_OKN = models.CharField(
        choices=information_CHOICES,
        max_length=5,
        verbose_name='Наличие паспорта ОКН'
    )
    actual_address = models.TextField(
        verbose_name='Актуальный адрес'
    )
    gen_species_appearance = models.ForeignKey(
        'Species',
        on_delete=models.CASCADE,
        verbose_name='Общая видовая принадлежность'
    )
    has_docs_boundaries = models.BooleanField(
        verbose_name='Наличие документов о границах территории ОКН'
    )
    req_of_approval = models.TextField(
        verbose_name='Реквизиты об утверждении границ территории'
    )
    has_docs_of_aprroval = models.BooleanField(
        verbose_name='Наличие документов об утвержденых зонах охраны'
    )
    document_on_approved_security = models.TextField(
        verbose_name='Документ об утвержденых зонах охраны'
    )
    has_rights = models.BooleanField(
        verbose_name='Наличие зарегистрированных прав/обременений'
    )
    date = models.DateField(
        verbose_name='Дата'
    )

    def __str__(self):
        return self.nativeName


class Municipality(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Муниципальное образование'
    )

    def __str__(self):
        return self.name


class Locality(models.Model):
    name = models.CharField(
        verbose_name='Населенный пункт',
        max_length=200
    )

    def __str__(self):
        return self.name


class Species(models.Model):
    name = models.CharField(
        verbose_name='Общая видовая принадлежность',
        max_length=200
    )

    def __str__(self):
        return self.name