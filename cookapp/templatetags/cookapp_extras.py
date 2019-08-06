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
def init_counter():
   delay_counter.count=0