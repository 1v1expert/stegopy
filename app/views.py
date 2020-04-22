from django.shortcuts import render
from app.forms import UploadDataForm


def index_view(request):
    if request.method == 'POST':
        form = UploadDataForm(request.POST, request.FILES)
        
        if form.is_valid():
            pass
    else:
        form = UploadDataForm()
    return render(request, 'index.html', {'form': form})
