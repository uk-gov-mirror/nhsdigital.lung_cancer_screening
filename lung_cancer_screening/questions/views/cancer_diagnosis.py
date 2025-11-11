from django.shortcuts import render, redirect
from django.urls import reverse

from .decorators.participant_decorators import require_participant

@require_participant
def cancer_diagnosis(request):
    if request.method == "POST":
        return redirect(reverse("questions:family_history_lung_cancer"))
    return render_template(
        request
    )

def render_template(request, status=200):
    return render(
        request,
        "question_form.jinja",
        {
            "back_link_url": reverse("questions:asbestos_exposure")
        },
        status=status
    )
