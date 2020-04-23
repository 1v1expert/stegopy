from django.shortcuts import render, redirect
from app.forms import UploadDataForm
from app.models import Steganographic
from app.utils.JuliaFractal import FractalImage


def index_view(request):
    if request.method == 'POST':
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            fractal = FractalImage(default_palette=True, pk=form.instance.pk).generate()
            form.instance.fractal_key_image = fractal.filename
            form.instance.save()
            return redirect('app:result', form.instance.pk)
    else:
        form = UploadDataForm()
    return render(request, 'index.html', {'form': form})


def result_view(request, result_id=None):
    if result_id is None:
        return redirect('app:index')
    
    return render(request, 'result.html', {'steganographic': Steganographic.objects.get(pk=result_id)})