from django.shortcuts import render, redirect
from .models import *
from .forms import EnrollForm
from django.contrib import messages
from .utils import can_add_subject_ects, can_add_subject_prev_ects

# Create your views here.
def home(request):
    return render(request, "home.html")

# Student
def student_list(request):
    students = Korisnik.objects.filter(role="STUDENT")
    context = {
        "students": students,
    }
    return render(request, "student_list.html", context)

# Enroll
def enroll_paper(request, student_id):
    student = Korisnik.objects.get(id=student_id)
    subjects = Subject.objects.all()

    enroll_paper = student.enroll_set.all()
    enrolled_subjects = enroll_paper.values_list('predmet', flat=True)

    num_of_semesters = student.status == 'REDOVNI' and 7 or 9
        
    context = {
        "student": student,
        "subjects": subjects,
        "enroll_paper": enroll_paper,
        "range": range(1, num_of_semesters),
        "enrolled_subjects": enrolled_subjects
    }
    return render(request, "enroll_paper.html", context)

def remove_enrolled_subject(request, enroll_id):
    enroll_subject = Enroll.objects.get(id=enroll_id)
    student_id = enroll_subject.student.id
    enroll_subject.delete()
    return redirect('enroll_paper', student_id=student_id)

def add_enrolled_subject(request):
    if request.method == 'POST':
        status = 'enrolled'
        student_id = request.POST['student_id']
        subject_id = request.POST['predmet_id']

        student = Korisnik.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)

        selected_status = student.status
        selected_semester = selected_status == 'REDOVNI' and subject.sem_redovni or subject.sem_izvanredni

        isEctsValid = can_add_subject_ects(student, subject, selected_semester)
        if isEctsValid == False:
            messages.error(request, f"Too much ECTS for {selected_semester}. semester")
            return redirect('enroll_paper', student_id=student_id)
        
        isPrevEctsValid = can_add_subject_prev_ects(student, subject, selected_semester)
        if isPrevEctsValid == False:
            messages.error(request, "Not enought points from previous semesters")
            return redirect('enroll_paper', student_id=student_id)


        Enroll.objects.create(student=student, predmet=subject, status=status)
        return redirect('enroll_paper', student_id=student_id)
    return render(request, "home.html")

def update_enrolled_subject(request, enroll_id):
    enroll_subject = Enroll.objects.get(id=enroll_id)
    student_id = enroll_subject.student.id
    status_update = enroll_subject.status == 'enrolled' and 'passed' or 'enrolled'
    enroll_subject.status = status_update
    enroll_subject.save()
    return redirect('enroll_paper', student_id=student_id)

# Course
def subject_list(request):
    subjects = Subject.objects.all()
    context = {
        "subjects": subjects,
    }
    return render(request, "subject_list.html", context)

def subject_details(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    context = {
        "subject": subject
    }
    return render(request, "subject_details", context)