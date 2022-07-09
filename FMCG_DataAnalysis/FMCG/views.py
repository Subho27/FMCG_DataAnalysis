from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from manage_data.materials import df
import json

# Create your views here.

def home(request):
    return render(request, 'home.html');

def viewdata(request):
    return render(request, 'viewdata.html');

def analysis(request):
    return render(request, 'analysis.html');

def mat_analysis(request):
    return render(request, 'mat_analysis.html');

def prediction(request):
    return render(request, 'prediction.html');

@csrf_exempt
def materials(request):
    result = df
    if request.is_ajax():
        param1 = request.GET.get('param1', None)
        param2 = request.GET.get('param2', None)
        result = result.loc[result['RM_PM'] == param1]
        json_records = result.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
        context = { 'data' : data}
        print(len(context['data']))
        return render(request, 'table.html', context);
    else:
        json_records = df.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
        context = { 'data' : data}
        print(len(context['data']))
        return render(request, 'materials.html', context);