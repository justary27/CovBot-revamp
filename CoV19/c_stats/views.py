from django.shortcuts import render
import requests
from requests.api import get
import covid
from covid import Covid
import datetime
from datetime import date
import json
import os
from dotenv import load_dotenv

load_dotenv()

list_cont = []

chart_cases = [['date','active','recovered','total']]

covid = Covid()

#covid functions
def country_list():
    countries = covid.list_countries()
    for i in range(len(countries)):
        x = countries[i]
        list_cont.append(x['name'])
    return list_cont

def active_cases(country):
    list_cases = covid.get_status_by_country_name(country)
    # print(list_cases)
    container = []
    container.append(list_cases['confirmed'])
    container.append(list_cases['active'])
    container.append(list_cases['deaths'])
    return container

def get_data_by_date(country,date,d_short):
    url = "https://covid-193.p.rapidapi.com/history"
    querystring = {"country":country,"day":date}
    headers = {
        'x-rapidapi-key': os.getenv("COVID_API"),
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.tex    
    res = json.loads(data)
    data = res['response']
    data = data[0]['cases']
    cases_today = []
    cases_today.append(d_short)
    cases_today.append(data['active'])
    
    cases_today.append(data['recovered'])
    cases_today.append(data['total'])
    
    return cases_today

def graph(country):
    today = date.today()
    d1 = datetime.datetime.now()
    arr = [['date','active','recovered','total']]
    for i in range (0,150,10):
        d2 = datetime.timedelta(days = i)
        d2 = d1 - d2
        d_form = d2.strftime("%Y-%m-%d")
        d_short = d2.strftime("%d %b")
        x = get_data_by_date(country,d_form,d_short)
        chart_cases.append(x)
    n = len(chart_cases)
    for i in range (n-1):
        arr.append(chart_cases[n-i-1])
    return arr

def country_list():
    countries = covid.list_countries()
    for i in range(len(countries)):
        if i<=4:
            x = countries[i]
            list_cont.append(x['name'])
    return list_cont


# a_list=[]
# def countryactive_list():
    # countries = covid.list_countries()
    # for i in range(len(countries)):
        # if i<=4:
            # x = countries[i]
            # a_list.append(active_cases(str(x['name'])))
    # return a_list

w_active= covid.get_total_active_cases()
w_deaths= covid.get_total_deaths()
w_confirmed= covid.get_total_confirmed_cases()
top_countries=country_list()
top1=active_cases(top_countries[0])
top2=active_cases(top_countries[1])
top3=active_cases(top_countries[2])
top4=active_cases(top_countries[3])
top5=active_cases(top_countries[4])


# Create your views here.
def index(request):
    context={
    'w_active':w_active,
    'w_confirmed':w_confirmed,
    'w_deaths':w_deaths,
    'top_countries':top_countries,
    'top1':top1,
    'top2':top2,
    'top3':top3,
    'top4':top4,
    'top5':top5,
    # 'top_active_countries':top_active_countries,
    }
    return render(request,r'c_stats\stats.html',context)