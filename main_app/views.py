from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request')

        if special_request :
            print(name,email,service,service_date,special_request)
        else :
            print(name,email,service,service_date)
        return redirect('thank_u')
    return render(request,'index.html')


def about(request):
    return render(request,'about_us.html')

def serive(request):
    return render(request,'service.html')

def mission(request):
    return render(request,'mission.html')

def contact(request):
    if request.method == 'POST':
        # Retrieve form data directly from request.POST
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Process the form data (e.g., save to database, send an email)
        # Example: Print form data to the console
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Number: {number}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        return redirect('thank_u')
    return render(request,'contact.html')

def faq(request):
    return render(request,'faq.html')

def feedback(request):
    if request.method == 'POST':
        feed_first_name = request.POST.get('q8_name[first]')
        feed_last_name = request.POST.get('q8_name[last]')
        feed_email = request.POST.get('q6_email6')
        feed_feedback_type = request.POST.get('q3_feedbackType')
        feed_feedback_description = request.POST.get('q4_describeYour')

        # Process the data, e.g., save it to the database, send an email, etc.
        # Example: Just printing to the console for now
        print(f"Name: {feed_first_name} {feed_last_name}")
        print(f"Email: {feed_email}")
        print(f"Feedback Type: {feed_feedback_type}")
        print(f"Feedback: {feed_feedback_description}")
        return redirect('thank_u')
    return render(request,'feedback.html')

def career(request):
    if request.method == 'POST':
        first_name = request.POST.get('q13_name[first]')
        last_name = request.POST.get('q13_name[last]')
        dob = request.POST.get('dob')
        email = request.POST.get('q14_email')
        phone = request.POST.get('q27_phoneNumber[full]')
        job_position = request.POST.get('q16_jobPosition')
        department = request.POST.get('q18_department')
        cv_link = request.POST.get('q17_supervisorsName[first]')

        # Process the form data (e.g., save to database, send an email)
        # Example: Print form data to the console
        print(f"Name: {first_name} {last_name}")
        print(f"Date of Birth: {dob}")
        print(f"Email: {email}")
        print(f"Phone: {phone}")
        print(f"Job Position: {job_position}")
        print(f"Department: {department}")
        print(f"CV Link: {cv_link}")
        return redirect('thank_u')
    return render(request,'career.html')

def req(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request')

        if special_request :
            print(name,email,service,service_date,special_request)
        else :
            print(name,email,service,service_date)
        return redirect('thank_u')
    return render(request,'request.html')

def thank_u(request):
    
    return render(request,'thank_u.html')

def vision(request):
    
    return render(request,'vision.html')