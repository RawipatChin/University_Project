from django.http.response import HttpResponse
from django.shortcuts import render

all_cloths = [
    {'id' : 1, 'title': 'ฟ้าแจ่มใส แดดออก แดดแรง ไม่เกรงใจใคร',}, 
    {'id' : 2, 'title': 'ฟ้าครึ้ม มืดมน มืดดำ เหงาหงอย'}, 
    {'id' : 3, 'title': 'ลมหนาว เศร้าสร้อย เหน็บหนาว ไร้คนกอด'},
]

# Create your views here.

def cloths(request):
    context = { 'cloths': all_cloths }
    return render(request, 'app_cloths/cloths.html', context)

def cloth(request, cloth_id):
    one_cloth = None
    try:
        one_cloth = [f for f in all_cloths if f['id'] == cloth_id][0]
    except IndexError:
        print('ไม่พบข้อมูลนี้')
    context = { 'cloth': one_cloth }
    return render(request, 'app_cloths/cloth.html', context)