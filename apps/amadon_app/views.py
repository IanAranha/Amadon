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
    print request.POST['item_id']
    for item in items:
        if item['item_id'] == request.POST['item_id']:
            print 'FINALLY!'
        else:
            print 'Item does not exist!'
        current_charge = item['price'] * int(request.POST['quantity'])
        current_charge = item['price'] * int(request.POST['quantity'])
        print current_charge
    print '*' * 10
    print request.POST
    return redirect('/checkout')

def checkout(request):
    return redirect('/')