from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Description, Comment


def index(request):
    errors = {}

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        desc_content = request.POST.get('description', '').strip()

        # Validation
        if len(name) <= 5:
            errors['name'] = 'Course name must be more than 5 characters long.'
        if len(desc_content) <= 15:
            errors['description'] = 'Description must be more than 15 characters long.'

        if not errors:
            course = Course.objects.create(name=name)
            Description.objects.create(content=desc_content, course=course)
            return redirect('index')

        # Re-render with errors and previously entered values
        return render(request, 'courses_app/index.html', {
            'courses': Course.objects.all().order_by('-created_at'),
            'errors': errors,
            'name_val': name,
            'desc_val': desc_content,
        })

    courses = Course.objects.all().order_by('-created_at')
    return render(request, 'courses_app/index.html', {'courses': courses, 'errors': {}})


def destroy(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'yes':
            course.delete()
        return redirect('index')

    # GET — show confirmation page
    return render(request, 'courses_app/destroy.html', {'course': course})


def comments(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    errors = {}

    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if not content:
            errors['content'] = 'Comment cannot be empty.'
        else:
            Comment.objects.create(content=content, course=course)
            return redirect('comments', course_id=course_id)

    all_comments = course.comments.all().order_by('-created_at')
    return render(request, 'courses_app/comments.html', {
        'course': course,
        'comments': all_comments,
        'errors': errors,
    })
