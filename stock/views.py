import logging
from django.conf import settings as conf_settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import connection
from django.http import FileResponse
from django.shortcuts import render, redirect

from .price_fetch import load_orchestrator
log = logging.getLogger('local_log')

def test_db(request):
    log.info('Start')
    template = "home.html"
    context = {

    }
    outcome = load_orchestrator()
    # return render(request, template, context)
    return redirect('home')
