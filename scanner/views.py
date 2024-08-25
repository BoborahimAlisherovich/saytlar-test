from django.shortcuts import render
from .forms import URLForm
from .scanner import scan_vulnerabilities

def scan_view(request):
    form = URLForm()
    vulnerabilities = []
    message = ""

    if request.method == "POST":
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            vulnerabilities = scan_vulnerabilities(url)
            if not vulnerabilities:
                message = "No vulnerabilities found. The website is secure."
    
    context = {
        'form': form,
        'vulnerabilities': vulnerabilities,
        'message': message,
    }
    
    return render(request, 'scan.html', context)
