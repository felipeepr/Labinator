from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.utils import timezone

from .models import Samples, Result

def index(request):
    latest_sample_list = Samples.objects.order_by("sample_date")[:5]
    context = {"latest_sample_list": latest_sample_list}
    return render(request, "samplesAnalyzer/index.html", context)

def detail(request, sample_name):
    sample = get_object_or_404(Samples, sample_name=sample_name)
    return render(request, "samplesAnalyzer/detail.html", {"sample": sample})

def results(request, sample_id, result):
    sample = get_object_or_404(Samples, pk=sample_id)
    return render(request, "samplesAnalyzer/results.html", {"sample": sample, "result": result})

def tested(request, sample_id):
    sample = get_object_or_404(Samples, pk=sample_id)
    if request.method == "POST":
        result = request.POST["result"]
        Result.objects.update_or_create(
            samples=sample,
            defaults={
                "result_sample": sample.sample_name,
                "result_result": result,
                "result_date": timezone.now(),
            }
        )
        return HttpResponseRedirect(
            reverse("samplesAnalyzer:results", args=(sample.id, result))
        )
    
def samples_create(request):
    if request.method == "POST":
        name = request.POST["sample_name"]
        indicator = request.POST["sample_pacient_name"]
        date = request.POST["sample_date"]
        image=request.FILES.get("sample_image")
        Samples.objects.create(sample_name=name, sample_pacient_name=indicator, sample_date=date, sample_image=image)
        return HttpResponseRedirect(reverse("samplesAnalyzer:index"))
    return render(request, "samplesAnalyzer/index.html")

def samples_edit(request, sample_id):
    if request.method == "POST":
        Samples.objects.filter(pk=sample_id).update(
        sample_name = request.POST["sample_name"],
        sample_pacient_name = request.POST["sample_pacient_name"],
        sample_date = request.POST["sample_date"],)
        return HttpResponseRedirect(reverse("samplesAnalyzer:index"))
    sample = Samples.objects.get(pk=sample_id)
    return render(request, "samplesAnalyzer/index.html", {"sample": sample})

def samples_delete(request, sample_id):
    sample = get_object_or_404(Samples, pk=sample_id)
    if request.method == "POST":
        sampleDel = Samples.objects.filter(pk=sample_id)
        sampleDel.delete()
        return HttpResponseRedirect(reverse("samplesAnalyzer:index"))
    return render(request, "samplesAnalyzer/index.html", {"sample": sample})

def finalResults(request):
    results = Result.objects.all()
    sample = Samples.sample_pacient_name
    return render(request, "samplesAnalyzer/finalResults.html", {"results": results, "sample": sample})