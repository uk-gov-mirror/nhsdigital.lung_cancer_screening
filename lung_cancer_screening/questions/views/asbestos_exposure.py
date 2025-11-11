from django.shortcuts import render, redirect
from django.urls import reverse

from .decorators.participant_decorators import require_participant

@require_participant
def asbestos_exposure(request):
    if request.method == "POST":
        return redirect(reverse("questions:cancer_diagnosis"))
    return render_template(
        request
    )

def render_template(request, status=200):
    return render(
        request,
        "question_form.jinja",
        {
            "back_link_url": reverse("questions:respiratory_conditions")
        },
        status=status
    )
