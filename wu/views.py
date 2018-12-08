from django.shortcuts import render
import requests
import json
from .models import UserInfo
# Create your views here.
def home(request):
    api_request = requests.get('https://api.github.com/users?since=4')
    api = json.loads(api_request.content)
    for i in api:
        name = i['login']
        url = i['avatar_url']
        UserInfo.objects.create(
            name=name,
            url=url,
        )
    return render(request,'home.html',{"api":api})
def user(request):
    if request.method=='POST':
        user = request.POST['user']
        user_request = requests.get('https://api.github.com/users/'+user)
        username = json.loads(user_request.content)
        return render(request,'user.html',{'username':username})
    else:
        notfound = '请在搜索框中输入用户名'
        return render(request,'user.html',{'notfound':notfound})