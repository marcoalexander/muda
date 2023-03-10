from django.shortcuts import render

def indexExample(request):
    exampleText = "This is an example of dynamically sending data to a template file using Django's template formatting."
    return render(request, 'exampleIndex.html', {'exampleText': exampleText})