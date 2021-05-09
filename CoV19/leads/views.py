from os import path
from django.shortcuts import render
import gspread

# def get_sheets():
    # gc  = gspread.service_account(path='/src/covbot/credentials.json')
    # sh = gc.open('trail')
    # worksheet = sh.sheet1
    # res = worksheet.get_all_values()
    # return res # ['name','state','city','phone','verified T/F','leads']

# alpha=get_sheets()
# Create your views here.
def index(request):
    # context={
        # 'alpha':alpha
    # }
    return render(request,'leads/leads.html')
