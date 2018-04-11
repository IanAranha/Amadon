# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse 
from products import items


# Create your views here.
def index(request):
    context = {
        'items' : items
    }
    return render (request, 'amadon_app/index.html', context)

def buy(request, item_id, methods = 'POST'):
    print '*' * 10
    print item_id
    print request.POST
    return redirect('/checkout')

def checkout(request):
    return redirect('/')