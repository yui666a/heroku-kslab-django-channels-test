from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'daihugo/index.html') # ./templates/daihugo/index.htmlを参照

def index_template(request):
    ### 方法１
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # context = {'latest_question_list': latest_question_list}
    # return render(request, 'daihugo/index.html', context)

    ### 方法２
    # return render(request, 'index.html')

    ### 方法３
    return HttpResponse("大富豪ページへようこそ.（ここに直接書き込むのもあり?）")