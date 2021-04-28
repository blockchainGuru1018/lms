from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url

from rezepturen.models import (
                            Comment,
                            Rezeptur,
                            MaterialFaser,
                            MaterialBindemittel,
                            MaterialSieb,
                        )




@login_required
def administrator(request):
    context = {
        'comment_count': Comment.objects.all().count(),
        'rezepturen_count':Rezeptur.objects.all().count(),
        'materialfaser_count':MaterialFaser.objects.all().count(),
        'bindemittel_count':MaterialBindemittel.objects.all().count(),
        'sieb_count':MaterialSieb.objects.all().count(), }
    return render(request=request, context=context, template_name='administrator/index.html')
