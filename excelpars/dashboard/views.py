from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.db.models import Q
from .forms import LoginForm
from .models import ObjectInfo, Municipality, Locality, Species
from .forms import ObjectInfoForm


import json


def home(request):
    if not request.user.is_authenticated():
        return redirect(reverse('login'))
    else:
        return redirect(reverse('panel'))

    row = ObjectInfo.objects.get(id=1)
    data = print(row)
    return render(request, 'dashboard/home.html', {'text': data})


def login_view(request):
    form = LoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/panel')

    return render(request, 'dashboard/login.html', {'form': form})


@login_required
def panel(request):
    data = ObjectInfo.objects.all()
    form = ObjectInfoForm()
    return render(request, 'dashboard/panel.html', {'data': data, 'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/login')


def get_id_data(request):

    id = request.GET.get('id_row')
    row = ObjectInfo.objects.get(id=id)
    # data = serializers('json', row)
    data = serializers.serialize("json", [row, ])
    struct = json.loads(data)
    data = json.dumps(struct[0])
    # print(data)

    """data = {
        'id_openData': str(row.id_openData),
        'nativeName': str(row.nativeName),
        'fullAddress': str(row.fullAddress),
        'municipality_id': str(row.municipality_id),
        'locality_id': str(row.locality_id),
        'OKN_in_ensemble': str(row.OKN_in_ensemble),
        'information_sign': str(row.information_sign),
        'information_sign_photo': str(row.information_sign_photo),
        'information_sign_conformity': str(row.information_sign_conformity),
        'photo': str(row.photo),
        'url': str(row.url),
        'description': str(row.description),
        'affiliation_U': str(row.affiliation_U),
        'esp_valuable_object': str(row.esp_valuable_object),
        'requisites_and_title': str(row.requisites_and_title),
        'owner': str(row.owner),
        'management': str(row.management),
        'owner_contacts': str(row.owner_contacts),
        'has_security_obligation': str(row.has_security_obligation),
        'has_passport_OKN': str(row.has_passport_OKN),
        'actual_address': str(row.actual_address),
        'gen_species_appearance': str(row.gen_species_appearance),
        'has_docs_boundaries':str( row.has_docs_boundaries),
        'req_of_approval': str(row.req_of_approval),
        'has_docs_of_aprroval': str(row.has_docs_of_aprroval),
        'document_on_approved_security': str(row.document_on_approved_security),
        'has_rights': str(row.has_rights),
        'date': str(row.date),
    }"""
    # return HttpResponse(data, content_type='application/json')
    return HttpResponse(data)


def edit_data(request):
    print(request.POST)
    id_row_data = request.POST.get('id_row_data')
    id_openData = request.POST.get('id_openData')
    nativeName = request.POST.get('nativeName')
    fullAddress = request.POST.get('fullAddress')
    municipality = request.POST.get('municipality')
    locality = request.POST.get('locality')
    information_sign = request.POST.get('information_sign')
    information_sign_photo = request.POST.get('information_sign_photo')
    photo = request.POST.get('photo')
    url = request.POST.get('url')
    description = request.POST.get('description')

    requisites_and_title = request.POST.get('requisites_and_title')
    owner = request.POST.get('owner')
    management = request.POST.get('management')
    owner_contacts = request.POST.get('owner_contacts')
    has_security_obligation = request.POST.get('has_security_obligation')
    has_passport_OKN = request.POST.get('has_passport_OKN')
    actual_address = request.POST.get('actual_address')
    gen_species_appearance = request.POST.get('gen_species_appearance')
    req_of_approval = request.POST.get('req_of_approval')
    document_on_approved_security = request.POST.get('document_on_approved_security')
    date = request.POST.get('date')


    OKN_in_ensemble =  True if 'OKN_in_ensemble' in request.POST else  False
    affiliation_U = True if 'affiliation_U' in request.POST else False
    esp_valuable_object = True if 'esp_valuable_object' in request.POST else False
    has_docs_boundaries = True if 'has_docs_boundaries' in request.POST else False
    has_docs_of_aprroval = True if 'has_docs_of_aprroval' in request.POST else False
    has_rights = True if 'has_rights' in request.POST else False
    information_sign_conformity = True if 'information_sign_conformity' in request.POST else False

    print(affiliation_U)
    print(esp_valuable_object)
    print(has_docs_boundaries)
    print(has_docs_of_aprroval)
    print(information_sign_conformity)
    print(OKN_in_ensemble)

    if request.POST:
        data_row = ObjectInfo.objects.get(id=id_row_data)

        data_row.id_openData = id_openData
        data_row.nativeName = nativeName
        data_row.fullAddress = fullAddress

        data_row.municipality = Municipality.objects.get(id=int(municipality))

        data_row.locality = Locality.objects.get(id=locality)
        data_row.OKN_in_ensemble = OKN_in_ensemble
        data_row.information_sign = information_sign
        data_row.information_sign_photo = information_sign_photo
        data_row.information_sign_conformity = information_sign_conformity
        data_row.photo = photo
        data_row.url = url
        data_row.description = description

        data_row.affiliation_U = affiliation_U

        data_row.esp_valuable_object = esp_valuable_object

        data_row.requisites_and_title = requisites_and_title
        data_row.owner = owner
        data_row.management = management
        data_row.has_security_obligation = has_security_obligation
        data_row.has_passport_OKN = has_passport_OKN
        data_row.actual_address = actual_address
        data_row.gen_species_appearance = Species.objects.get(id=gen_species_appearance)

        data_row.has_docs_boundaries = has_docs_boundaries
        data_row.req_of_approval = req_of_approval
        data_row.has_docs_of_aprroval = has_docs_of_aprroval
        data_row.document_on_approved_security = document_on_approved_security
        data_row.has_rights = has_rights

        # data_row.date = date'''
        data_row.save()
        # print(id_openData)
        # print(data_row)

    return HttpResponseRedirect('http://127.0.0.1:8000/dashboard/panel/')


def add_data(request):
    print('in 1')
    text = ''
    if request.method == 'POST':
        print('in 2')
        form = ObjectInfoForm(request.POST)
        if form.is_valid():
            print('in 3')

            id_openData = form.cleaned_data['id_openData']
            nativeName = form.cleaned_data['nativeName']
            fullAddress = form.cleaned_data['fullAddress']
            municipality = form.cleaned_data['municipality']
            # municipality = request.POST.get('municipality')
            locality = form.cleaned_data['locality']
            # locality = request.POST.get('municipality')
            OKN_in_ensemble = form.cleaned_data['OKN_in_ensemble']
            information_sign = form.cleaned_data['information_sign']
            information_sign_photo = form.cleaned_data['information_sign_photo']
            information_sign_conformity = form.cleaned_data['information_sign_conformity']
            photo = form.cleaned_data['photo']
            url = form.cleaned_data['url']
            description = form.cleaned_data['description']
            affiliation_U = form.cleaned_data['affiliation_U']
            esp_valuable_object = form.cleaned_data['esp_valuable_object']
            requisites_and_title = form.cleaned_data['requisites_and_title']
            owner = form.cleaned_data['owner']
            management = form.cleaned_data['management']
            owner_contacts = form.cleaned_data['owner_contacts']
            has_security_obligation = form.cleaned_data['has_security_obligation']
            has_passport_OKN = form.cleaned_data['has_passport_OKN']
            actual_address = form.cleaned_data['actual_address']
            gen_species_appearance = form.cleaned_data['gen_species_appearance']
            has_docs_boundaries = form.cleaned_data['has_docs_boundaries']
            req_of_approval = form.cleaned_data['req_of_approval']
            has_docs_of_aprroval = form.cleaned_data['has_docs_of_aprroval']
            document_on_approved_security = form.cleaned_data['document_on_approved_security']
            has_rights = form.cleaned_data['has_rights']
            date = form.cleaned_data['date']

            print(type(municipality))
            print(type(locality))
            print(date)

            ObjectInfo.objects.create(
                id_openData=id_openData,
                nativeName=nativeName,
                fullAddress=fullAddress,
                municipality=municipality,
                # municipality=True,
                locality=locality,
                OKN_in_ensemble=OKN_in_ensemble,
                information_sign=information_sign,
                information_sign_photo=information_sign_photo,
                information_sign_conformity=information_sign_conformity,
                photo=photo,
                url=url,
                description=description,
                affiliation_U=affiliation_U,
                esp_valuable_object=esp_valuable_object,
                requisites_and_title=requisites_and_title,
                owner=owner,
                management=management,
                owner_contacts=owner_contacts,
                has_security_obligation=has_security_obligation,
                has_passport_OKN=has_passport_OKN,
                actual_address=actual_address,
                gen_species_appearance=gen_species_appearance,
                has_docs_boundaries=has_docs_boundaries,
                req_of_approval=req_of_approval,
                has_docs_of_aprroval=has_docs_of_aprroval,
                document_on_approved_security=document_on_approved_security,
                has_rights=has_rights,
                date=date,
            ).save()

            text = '''
            <div class="alert alert-success alert-dismissible fade show" role="alert">
              <strong></strong>Data was added.
              <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
            </div>
            '''
            print(form.cleaned_data)
    else:
        form = ObjectInfoForm()
    return render(request, 'dashboard/add_form.html', {"form": form, "text": text})


def search(request):
    query = request.GET.get('q')
    founded_articles = ObjectInfo.objects.filter(Q(id_openData__icontains=query) | Q(nativeName__icontains=query) | Q(fullAddress__icontains=query))
    form = ObjectInfoForm()
    context = {
        "data": founded_articles,
        "form": form
    }
    return render(request, "dashboard/panel.html", context)