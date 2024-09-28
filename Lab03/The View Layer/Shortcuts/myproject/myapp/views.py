# myapp/views.py
from django.shortcuts import render
from django.shortcuts import redirect

def my_view(request):
    # View code here...
    return render(
        request,
        "myapp/index.html",
        {
            "foo": "bar",
        },
        content_type="application/xhtml+xml",
    )
def redirect_view(request):
    # Chuyển hướng đến view 'my_view'
    return redirect('my_view')