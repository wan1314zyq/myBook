#coding=utf8
# @Author= CaiJunxuan
# @QQ=469590490
# @Wechat:15916454524
from django.shortcuts import render


def test(request):

	return render(request,'base.html')