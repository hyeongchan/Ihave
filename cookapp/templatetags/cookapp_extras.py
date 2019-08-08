# -*- coding: UTF-8 -*-
import logging
from django import template

register = template.Library()

@register.simple_tag
def test_tag():
   print("asdf")
   return 'test tag'


@register.filter            # 1
def current(left, right):
    return left

@register.simple_tag
def delay_counter():
   delay_counter.count += 0.1
   print("asdf")
   return delay_counter.count

@register.simple_tag
def counter():
   counter.count += 1
   print("asdf")
   return counter.count

@register.simple_tag
def init_delay_counter():
   delay_counter.count=0

@register.simple_tag
def init_counter():
   counter.count=0

@register.filter
def make_range(a,b):
   return filter(lambda a:a>0 and a<=b,range(a-2,a+3))

@register.filter
def active(a,b):
   if a==b:
      return "active"
   else:
      return ""

@register.filter
def value(a):
   if a=="/list/":
      return "재료 하나 추가!"
   else:
      return "원래 재료 보기!"