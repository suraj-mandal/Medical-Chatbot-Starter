from django.shortcuts import render

# Create your views here.

# list of symptoms
symptoms = []


# THIS IS THE DUMMY FUNCTION
# This function is taking the list of symptoms user in taking as input and then processing it
# TODO: REPLACE THIS FUNCTION WITH YOUR DRIVER CODE

def process_symptoms(symptoms_list):
    return [f'I am loving {symptom}' for symptom in symptoms_list]


def home(request):
    # just for searching the data and appending them in the current list of items
    # when request method is GET
    if request.method == 'GET':
        if 'user-symptoms' in request.GET:
            current_symptom = request.GET['user-symptoms']
            if current_symptom not in symptoms:
                symptoms.append(current_symptom)
        context = {
            'symptoms': symptoms
        }
        return render(request, 'symptoms/index.html', context=context)
    # when I am sending post data, I should not display the sensitive information on the address bar
    # when request method is POST
    else:
        predicted_diseases = process_symptoms(symptoms)
        symptoms.clear()
        context = {
            'predicted_diseases': predicted_diseases
        }
        return render(request, 'symptoms/index.html', context=context)
