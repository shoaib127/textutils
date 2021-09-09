#
# def about(request):
#     return  HttpResponse("hi this si about")
#
# def removepunc(request):
#     return  HttpResponse("remove punc")
#
# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("newlineremove")
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("char count")
#
#
# def challenge(request):
#     # s='''<h1>Entertainment <a href="https://www.google.com">google</a>'''
#     s=[
#         '''<h1>Entertainment</h1>''',
#         '''<a href="https://www.facebook.com">Facebook</a><br>''',
#         '''<a href="https://www.flipkart.com">Flipkart</a>"'''
#     ]
#
#     return  HttpResponse(s)

s = "jasdhsdsd dsadjasdsad asdd   sdnasdd"

for i,j in enumerate(s):
    print(i,j)