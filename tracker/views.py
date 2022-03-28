from django.shortcuts import render


# Create your views here.
def homepage(request):
    if request.method == "POST":
        print(request.POST["code"])
        # check if the code exists
        # if exists redirect to the meeting page and record data
    return render(request, 'homepage.html')
