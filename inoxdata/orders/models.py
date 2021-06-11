from django.db import models
from django.urls import reverse


class Orders(models.Model):
    name_order = models.CharField(max_length=255, verbose_name='Заказ')  # номер заказа
    part = models.ForeignKey('Parts', on_delete=models.PROTECT, verbose_name='Деталь')  # ссылка на деталь
    ready_qty = models.IntegerField(default=0)  # количество готовых деталей
    need_qty = models.IntegerField(verbose_name='Количество')  # требуемое количество деталей
    machine = models.ForeignKey('Machine', on_delete=models.PROTECT)  # станок для резки
    note = models.TextField(blank=True, verbose_name='Примечание')  # примечание (blank=True - значения может не быть)
    need_material = models.BooleanField(default=True, verbose_name='Материал в наличии')  # на будущее, есть ли материал
    date_for_ready = models.DateField(verbose_name='Дата выдачи заказчику')  # дата выдачи заказа клиенту
    otk = models.BooleanField(default=False, verbose_name='Одобрен')  # первая деталь в партии

    def __str__(self):
        return str(self.name_order)

    def get_absolute_url(self):
        return reverse('form_orders')


class Parts(models.Model):
    name_part = models.CharField(max_length=255, verbose_name='Деталь')  # название детали
    material = models.ForeignKey('Materials', verbose_name='Материал', on_delete=models.PROTECT)  # ссылка на материал
    thickness = models.ForeignKey('Thickness', verbose_name='Толщина', on_delete=models.PROTECT)  # толщина материала
    cut_length = models.IntegerField(verbose_name='Длина реза(мм)')  # длина реза
    cut_input = models.IntegerField(verbose_name='Количество входов')  # количество входов
    x_length = models.IntegerField(verbose_name='Длина')  # длина детали
    y_length = models.IntegerField(verbose_name='Ширина')  # ширина детали
    fill_factor = models.FloatField(default=1, verbose_name='Фактор площади')  # коэффициент заполнения на листе
    # note = models.TextField(blank=True, verbose_name='Примечание')  # примечание (blank=True - значения может не быть)
    otk = models.BooleanField(default=False, verbose_name='Одобрен')  # отработана

    def __str__(self):
        return str(self.name_part)

    def get_absolute_url(self):
        return reverse('form_parts')


class Materials(models.Model):
    name_material = models.CharField(max_length=255, verbose_name='Материал')  # название материала

    def __str__(self):
        return str(self.name_material)

    def get_absolute_url(self):
        return reverse('form_materials')


class Thickness(models.Model):
    thickness = models.FloatField(verbose_name='Толщина')  # толщина материала

    def __str__(self):
        return str(self.thickness)

    def get_absolute_url(self):
        return reverse('form_thickness')


class ReadyOrders(models.Model):
    name_order = models.CharField(max_length=255)  # номер заказа
    part = models.ForeignKey('Parts', on_delete=models.PROTECT)  # ссылка на деталь
    need_qty = models.IntegerField()  # требуемое количество деталей
    note = models.TextField(blank=True)  # примечание (blank=True - значение может быть пустым)
    date_time_ready = models.DateTimeField(auto_now_add=True)  # время готовности
    material = models.ForeignKey('Materials', verbose_name='Материал', on_delete=models.PROTECT)  # если был использован
    thickness = models.ForeignKey('Thickness', verbose_name='Материал', on_delete=models.PROTECT)  # не стандартный мате
    otk = models.CharField(max_length=255)  # кто утвердил партию

    def get_absolute_url(self):
        return reverse('ready')


class Storage(models.Model):
    name = models.CharField(max_length=255)  # обозначение куска для идентификации
    material = models.ForeignKey('Materials', on_delete=models.PROTECT)  # ссылка на характеристики материала
    thickness = models.ForeignKey('Thickness', verbose_name='Материал', on_delete=models.PROTECT)  # толщина материала
    square = models.FloatField()  # количество материала в мкв
    place = models.CharField(max_length=255)  # место где искать кусок


class Machine(models.Model):
    name = models.CharField(max_length=255, verbose_name='Станок')  # станок

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('form_machine')
