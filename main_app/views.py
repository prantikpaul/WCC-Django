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

        # Create the email message
        subject = f"Service Request from {name}"
        if special_request:
            message = f"Name: {name}\nEmail: {email}\nService: {service}\nService Date: {service_date}\nSpecial Request: {special_request}"
        else:
            message = f"Name: {name}\nEmail: {email}\nService: {service}\nService Date: {service_date}"

        from_email = 'assassins81007@gmail.com'  # Replace with your Gmail
        recipient_list = ['assassins81007@gmail.com']  # Replace with your Gmail

        # Send the email
        send_mail(subject, message, from_email, recipient_list)

        # Redirect after sending the email
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

        subjectt = f"New contact form submission: {subject}"
        
        message = f"""
        Name: {name}
        Email: {email}
        Phone Number: {number}
        
        Message:
        {message}
        """

        from_email = 'assassins81007@gmail.com'  # Replace with your Gmail
        recipient_list = ['assassins81007@gmail.com']  # Replace with your Gmail

        # Send the email
        send_mail(subjectt, message, from_email, recipient_list)
        
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

        email_subject = f"New Feedback from {feed_first_name} {feed_last_name}"
        email_message = f"""
        Name: {feed_first_name} {feed_last_name}
        Email: {feed_email}
        Feedback Type: {feed_feedback_type}
        
        Feedback Description:
        {feed_feedback_description}
        """

        from_email = 'assassins81007@gmail.com'  # Replace with your Gmail
        recipient_list = ['assassins81007@gmail.com']  # Replace with your Gmail
        
        # Send the email
        send_mail(
            email_subject,
            email_message,
            from_email,  # From email (your email)
            recipient_list,  # To email (where you want the feedback)
        )
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

        email_subject = f"New Job Application: {first_name} {last_name} for {job_position}"
        email_message = f"""
        First Name: {first_name}
        Last Name: {last_name}
        Date of Birth: {dob}
        Email: {email}
        Phone Number: {phone}
        Job Position: {job_position}
        Department: {department}
        CV Link: {cv_link}
        """
        from_email = 'assassins81007@gmail.com'  # Replace with your Gmail
        recipient_list = ['assassins81007@gmail.com']  # Replace with your Gmail
        # Send the email
        send_mail(
            email_subject,
            email_message,
            from_email,  # From email (your email)
            recipient_list,  # To email where you want to send the data
        )
        
        # Redirect to a thank you page
        return redirect('thank_u')

        return redirect('thank_u')
    return render(request,'career.html')

def req(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        service_date = request.POST.get('service_date')
        special_request = request.POST.get('special_request')

        # Create the email message
        subject = f"Service Request from {name}"
        if special_request:
            message = f"Name: {name}\nEmail: {email}\nService: {service}\nService Date: {service_date}\nSpecial Request: {special_request}"
        else:
            message = f"Name: {name}\nEmail: {email}\nService: {service}\nService Date: {service_date}"

        from_email = 'assassins81007@gmail.com'  # Replace with your Gmail
        recipient_list = ['assassins81007@gmail.com']  # Replace with your Gmail

        # Send the email
        send_mail(subject, message, from_email, recipient_list)

        # Redirect after sending the email
        return redirect('thank_u')
    return render(request,'request.html')

def thank_u(request):
    
    return render(request,'thank_u.html')

def vision(request):
    
    return render(request,'vision.html')