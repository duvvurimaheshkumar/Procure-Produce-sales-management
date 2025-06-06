from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import ProducerSignUpForm
from .models import Producer,ProducerVerify

def producer(request):
    return render(request,'producer/producer.html')

def login(request):
    return render(request,'producer/login.html')


@csrf_protect
def signUp(request):
    if request.method == 'POST':
        
        form = ProducerSignUpForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['fname']
            last_name = form.cleaned_data['lname']
            email = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            postal = form.cleaned_data['postcode']
            address = form.cleaned_data['address']
            
            # Instantiate Producer
            producer = ProducerVerify.objects.create(
                firstName=first_name,
                lastName=last_name,
                email=email,
                contact=contact,
                postalcode=postal,
                address=address,
                pictures=request.FILES.get('pictures'),  # Assign uploaded pictures
                document=request.FILES.get('document')  # Assign uploaded document
            )
            producer.save()
            return render(request, 'producer/success.html')

    else:
        form = ProducerSignUpForm()

    return render(request, 'producer/signup.html', {'form': form})

def success(request):
    return render(request,'producer/success.html')
