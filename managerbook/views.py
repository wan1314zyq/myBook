from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
# ListView是专门做视图展示的一个方法

from managerbook.models import *

class index(ListView):
	'''
	首页	书籍列表	查询功能
	'''
	template_name = 'book.html'

	# 要展示哪个表的试图，需要导入试图
	model = Book
	context_object_name = 'book_obj'

