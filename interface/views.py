from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import ProjectIdea

def submit_idea(request):
    if request.method == "POST":
        try:
            name = request.POST.get("idea_name")
            email = request.POST.get("idea_email")   # student email
            college = request.POST.get("idea_college")
            branch = request.POST.get("idea_branch")
            domain = request.POST.get("idea_domain")
            description = request.POST.get("idea_description")
            requirements = request.POST.get("idea_requirements")
            budget = request.POST.get("idea_budget")
            deadline = request.POST.get("idea_deadline")

            # Save to DB
            ProjectIdea.objects.create(
                name=name,
                email=email,
                college=college,
                branch=branch,
                domain=domain,
                description=description,
                requirements=requirements,
                budget=budget,
                deadline=deadline,
            )

            # Email to Admin
            subject = "📩 New Project Idea Submitted"
            message = f"""
A new project idea has been submitted:

👤 Name: {name}
📧 Email: {email}
🏫 College: {college}
📚 Branch: {branch}
💡 Domain: {domain}
💰 Budget: ₹{budget}
📅 Deadline: {deadline}

📝 Description:
{description}

📋 Requirements:
{requirements}
"""
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,            # from
                ["destfinder9564@gmail.com"],        # admin email
                fail_silently=False,
            )

            # Confirmation Email to Student
            student_subject = "✅ Thank you for submitting your Project Idea!"
            student_message = f"""
Hello {name},

We have received your project idea successfully. Our team will review it and get back to you soon.

Here are your submission details:
- Domain: {domain}
- Budget: ₹{budget}
- Deadline: {deadline}

Thank you for choosing Idea2Project!

Best Regards,  
Team Idea2Project
"""
            send_mail(
                student_subject,
                student_message,
                settings.EMAIL_HOST_USER,            # from
                [email],                             # student email
                fail_silently=True,
            )

            messages.success(request, "Your project idea has been submitted successfully! A confirmation email has been sent to you.")
            return redirect("home")

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect("home")

    return render(request, "home.html")

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import ProjectRequest

def need_project(request):
    if request.method == "POST":
        try:
            name = request.POST.get("need_name")
            college = request.POST.get("need_college")
            branch = request.POST.get("need_branch")
            domain = request.POST.get("need_domain") or "Not Specified"
            email = request.POST.get("need_email")
            budget = request.POST.get("need_budget")
            deadline = request.POST.get("need_deadline")

            # Save to DB
            ProjectRequest.objects.create(
                name=name,
                college=college,
                branch=branch,
                domain=domain,
                email=email,
                budget=budget,
                deadline=deadline,
            )

            # Send email to Admin
            subject = "📩 New Project Request Submitted"
            message = f"""
A new project request has been submitted:

👤 Name: {name}
📧 Email: {email}
🏫 College: {college}
📚 Branch: {branch}
💡 Domain: {domain}
💰 Budget: ₹{budget}
📅 Deadline: {deadline}
"""
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                ["destfinder9564@gmail.com"],   # admin email
                fail_silently=False,
            )

            # Confirmation Email to Student
            student_subject = "✅ Thank you for requesting a project!"
            student_message = f"""
Hello {name},

We have received your project request successfully. Our team will get back to you soon.

Here are your request details:
- Domain: {domain}
- Budget: ₹{budget}
- Deadline: {deadline}

Thank you for choosing Idea2Project!

Best Regards,  
Team Idea2Project
"""
            send_mail(
                student_subject,
                student_message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )

            messages.success(request, "Your project request has been submitted successfully! A confirmation email has been sent to you.")
            return redirect("home")

        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect("home")

    return render(request, "home.html")
