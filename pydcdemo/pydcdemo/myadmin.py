from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
import pymysql
import datetime
import os

conn=pymysql.connect(
    user='root',
    password='123456',
    port=3306,
    host='127.0.0.1',
    db='myshop',
    charset='utf8'
)
cursor=conn.cursor()
cursor.execute('set names utf8')
cursor.execute('set autocommit=1')


def test(request):
    return render(request, 'test.html')

def testdata(request):
    context = {}
    context['hello'] = '夜鹰教程网测试, 此处的数据来自于函数里面，不是模板里面，模板里面只是一个标记!'
    return render(request, 'testdata.html',context)

def hello(request):
    s="<h1 style='color:red;'>welcome to rongzhi</h1>"
    response = HttpResponse(s)
    #允许跨域使用
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "POST,GET,OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "*"
    return response

#渲染表单
@xframe_options_exempt
def foodadd(request):
    return render(request, 'foodadd.html')

#用来处理post提交的表单数据
@xframe_options_exempt
def foodaddpost(request):

    #接收参数
    tbname = request.POST.get('tbname')
    tbprice = request.POST.get('tbprice')
    tbbrief = request.POST.get('tbbrief')
    tbcontents = request.POST.get('tbcontents')

    fullname=""
    #图片上传开始
    imgurl = request.FILES.get('tbpic')
    if (str(imgurl) != "None"):#有文件上传的情况  # yxrs2.jpg    20200226144630.jpg   static/uploadimg/20200226144630.jpg
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")#s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  #获取的文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')
        extname = ""#这个变量用来保存扩展名
        if pos > 0:
            extname = oldname[pos:]   # .jpg把扩展名取出来保存在变量extname中
        fullname = s + extname  #用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  #拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")#把路径中的反斜杠替换为斜杠 static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:#没有上传文件的情况
        fullname = ""
    #图片上传结束

    strsql = "insert into tbproduct (proname,price,brief,descriptions,imgurl,address,typeid) values ('"+tbname+"',"+tbprice+",'"+tbbrief+"','"+tbcontents+"','"+fullname+"','重庆',1) "
    cursor.execute(strsql)
    return render(request, 'foodadd.html',{"msg":"保存成功"})

#渲染表单
@xframe_options_exempt
def drinkadd(request):
    return render(request, 'drinkadd.html')


#用来处理post提交的表单数据
@xframe_options_exempt
def drinkaddpost(request):

    #接收参数
    tbname = request.POST.get('tbname')
    tbprice = request.POST.get('tbprice')
    tbtype = request.POST.get('tbtype')

    fullname=""
    #图片上传开始
    imgurl = request.FILES.get('tbpic')
    if (str(imgurl) != "None"):#有文件上传的情况  # yxrs2.jpg    20200226144630.jpg   static/uploadimg/20200226144630.jpg
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")#s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  #获取的文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')
        extname = ""#这个变量用来保存扩展名
        if pos > 0:
            extname = oldname[pos:]   # .jpg把扩展名取出来保存在变量extname中
        fullname = s + extname  #用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  #拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")#把路径中的反斜杠替换为斜杠 static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:#没有上传文件的情况
        fullname = ""
    #图片上传结束

    strsql = "insert into tbdrink (proname,price,type,imgurl) values ('"+tbname+"',"+tbprice+",'"+tbtype+"','"+fullname+"') "
    cursor.execute(strsql)
    return render(request, 'drinkadd.html',{"msg":"保存成功"})

#允许在框架下加载
@xframe_options_exempt
def foodlist(request):
    strsql = "select id,proname,price,imgurl,brief from tbproduct order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    foodlist=[]
    while row:
        #print(row)
        foodlist.append({"id": row[0], "proname": row[1], "price": row[2],"imgurl": row[3],"brief": row[4]})
        row = cursor.fetchone()
    return render(request, 'foodlist.html',{'foodlist': foodlist})

#允许在框架下加载
@xframe_options_exempt
def drinklist(request):
    strsql = "select id,proname,price,imgurl,type from tbdrink order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    drinklist=[]
    while row:
        #print(row)
        drinklist.append({"id": row[0], "proname": row[1], "price": row[2],"imgurl": row[3],"type": row[4]})
        row = cursor.fetchone()
    return render(request, 'drinklist.html',{'drinklist': drinklist})

#允许在框架下加载
@xframe_options_exempt
def foodedit(request):
    id = request.GET.get("id")
    strsql1 = "select id,proname,price,imgurl,brief,descriptions,address  from tbproduct where id="+id
    cursor.execute(strsql1)
    row = cursor.fetchone()
    view={"id": row[0], "proname": row[1], "price": row[2],"imgurl": row[3],"brief": row[4],"descriptions": row[5],"address": row[6]}
    return render(request, 'foodedit.html',{'foodview': view})

#允许在框架下加载
@xframe_options_exempt
def drinkedit(request):
    id = request.GET.get("id")
    strsql1 = "select id,proname,price,imgurl,type from tbdrink where id="+id
    cursor.execute(strsql1)
    row = cursor.fetchone()
    view={"id": row[0], "proname": row[1], "price": row[2],"imgurl": row[3],"type": row[4]}
    return render(request, 'drinkedit.html',{'drinkview': view})

#上传菜品图片
@xframe_options_exempt
def foodeditpost(request):
    #接收参数
    proid = request.POST.get("proid")
    oldimgurl = request.POST.get("oldimgurl")

    tbname = request.POST.get("tbname")
    tbprice = request.POST.get("tbprice")
    tbbrief = request.POST.get("tbbrief")
    tbcontents = request.POST.get("tbcontents")

    imgurl = request.FILES.get('tbpic')

    fullname=""
    if(str(imgurl)!="None"):
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")
        oldname=imgurl.name
        pos = oldname.rfind('.')
        extname=""
        if pos > 0:
            extname= oldname[pos:]
        fullname=s+extname
        file_path = os.path.join('static/uploadimg', fullname)
        file_path=file_path.replace("\\","/")
        print(file_path)
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:
        fullname=oldimgurl

    sqlstr = "update tbproduct set proname='"+tbname+"',price="+tbprice+",brief='"+tbbrief+"',descriptions='"+tbcontents+"',imgurl='"+fullname+"' where id="+proid
    cursor.execute(sqlstr)
    conn.commit()
    view = {"id": proid, "proname": tbname, "price": tbprice, "imgurl": fullname, "brief": tbbrief, "descriptions": tbcontents,
            "address":"","msg":"保存成功"}
    return render(request, 'foodedit.html',{'foodview': view})


#上传酒水图片
@xframe_options_exempt
def drinkeditpost(request):
    #接收参数
    proid = request.POST.get("proid")
    oldimgurl = request.POST.get("oldimgurl")

    tbname = request.POST.get("tbname")
    tbprice = request.POST.get("tbprice")
    tbtype = request.POST.get("tbtype")

    imgurl = request.FILES.get('tbpic')

    fullname=""
    if(str(imgurl)!="None"):
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")
        oldname=imgurl.name
        pos = oldname.rfind('.')
        extname=""
        if pos > 0:
            extname= oldname[pos:]
        fullname=s+extname
        file_path = os.path.join('static/uploadimg', fullname)
        file_path=file_path.replace("\\","/")
        print(file_path)
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:
        fullname=oldimgurl

    sqlstr = "update tbproduct set proname='"+tbname+"',price="+tbprice+",brief='"+tbtype+"',imgurl='"+fullname+"' where id="+proid
    cursor.execute(sqlstr)
    conn.commit()
    view = {"id": proid, "proname": tbname, "price": tbprice, "type": tbtype,"imgurl": fullname,"msg":"保存成功"}
    return render(request, 'drinkedit.html',{'drinkview': view})

@xframe_options_exempt
def fooddelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from tbproduct where id="+id
    cursor.execute(sqlstr1)
    conn.commit()
    #重新查询数据，渲染列表模板
    sqlstr2 = "select id,proname,price,imgurl,brief from tbproduct order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    foodlist = []
    while row:
        # print(row)
        foodlist.append({"id": row[0], "proname": row[1], "price": row[2], "imgurl": row[3], "brief": row[4]})
        row = cursor.fetchone()
    return render(request, 'foodlist.html', {'foodlist': foodlist})

@xframe_options_exempt
def drinkdelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from tbdrink where id="+id
    cursor.execute(sqlstr1)
    conn.commit()
    #重新查询数据，渲染列表模板
    sqlstr2 = "select id,proname,price,imgurl,type from tbdrink order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    drinklist = []
    while row:
        # print(row)
        drinklist.append({"id": row[0], "proname": row[1], "price": row[2], "imgurl": row[3], "type": row[4]})
        row = cursor.fetchone()
    return render(request, 'drinklist.html', {'drinklist': drinklist})

@xframe_options_exempt
def orderlist(request):
    strsql = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead order by id desc "
    cursor.execute(strsql)
    conn.commit()
    list = []
    row = cursor.fetchone()
    while row:
        list.append({"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],"memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9]})
        row = cursor.fetchone()
    return render(request, 'orderlist.html', {'list': list})

@xframe_options_exempt
def orderdelete(request):
    #接收参数 参数就是订单号
    orderid = request.GET.get("orderid")
    #根据订单号删除订单抬头表和订单明细表的数据
    strsql1="delete from tborderhead where orderid="+orderid
    strsql2 = "delete from tborderitems where orderid=" + orderid
    #因为我们在数据库里面建立了外键约束，所以删除的时候必须先删除明细表，再删除抬头表里面的订单信息。
    cursor.execute(strsql2)
    cursor.execute(strsql1)
    strsql = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead order by id desc "
    cursor.execute(strsql)
    conn.commit()
    #查询删除后的数据，把删除后的数据重新渲染显示在列表中
    list = []
    row = cursor.fetchone()
    while row:
        list.append(
            {"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],
             "memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9]})
        row = cursor.fetchone()
    return render(request, 'orderlist.html', {'list': list})


@xframe_options_exempt
def orderview(request):
    #根据订单的id把订单的抬头和订单的明细全部查询出来，查询出来的结果只包含当前这个订单的信息
    orderid = request.GET.get("orderid")
    strsql1 = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo from tborderhead where orderid=" + orderid
    strsql2 = "select id,orderid,proid,proname,price,procount,imgurl from tborderitems where orderid=" + orderid

    cursor.execute(strsql2)
    rowitem = cursor.fetchone()
    list = []
    while rowitem:
        list.append({"id": rowitem[0], "orderid": rowitem[1], "proid": rowitem[2], "proname": rowitem[3], "price": rowitem[4],"procount": rowitem[5],"imgurl": rowitem[6]})
        rowitem = cursor.fetchone()

    cursor.execute(strsql1)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    head = {"id": row[0], "orderid": row[1], "sname": row[2], "stel": row[3], "saddress": row[4], "sumprice": row[5],
            "memberid": row[6], "ctime": row[7], "ptime": row[8], "memo": row[9], "items": list}
    return render(request, 'orderview.html', {'obj': head})

@xframe_options_exempt
def login(request):
    return render(request, 'login.html')


@xframe_options_exempt
def loginpost(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    strsql="select id,username,truename from tbusers where username='"+username+"' and password='"+password+"'"
    cursor.execute(strsql)
    row = cursor.fetchone()
    context = {}
    if row:
        #如果成功 就跳转到主页面
        return redirect("/static/myadmin/default.html")
    else:
        #重新渲染登录页面
        context['msg'] = '用户名或者密码错误!'
        return render(request, 'login.html', context)



# 用来处理post提交的表单数据
@xframe_options_exempt
def lunbosetting(request):
    return render(request, 'lunbosetting.html')



@xframe_options_exempt
def lunbopost(request):

    # 接收参数
    # tbname = request.POST.get('tbname')

    fullname = ""
    # 图片上传开始
    imgurl = request.FILES.get('tbpic')
    if (str(imgurl) != "None"):  # 有文件上传的情况  # yxrs2.jpg    20200226144630.jpg   static/uploadimg/20200226144630.jpg
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取的文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:
            extname = oldname[pos:]  # .jpg把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠替换为斜杠 static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:  # 没有上传文件的情况
        fullname = ""
    # 图片上传结束

    strsql = "insert into lunboimg (imgurl) values ('"+fullname+"')"
    cursor.execute(strsql)
    return render(request, 'lunbosetting.html', {"msg": "保存成功"})

    # 允许在框架下加载




# 用来处理post提交的表单数据
@xframe_options_exempt
def privateroom(request):
    return render(request, 'privateroom.html')



@xframe_options_exempt
def roompost(request):

    # 接收参数
    tbname = request.POST.get('tbname')
    tbprice = request.POST.get('tbprice')
    tbbrief = request.POST.get('tbbrief')


    fullname = ""
    # 图片上传开始
    imgurl = request.FILES.get('tbpic')
    if (str(imgurl) != "None"):  # 有文件上传的情况  # yxrs2.jpg    20200226144630.jpg   static/uploadimg/20200226144630.jpg
        t = datetime.datetime.today()
        s = datetime.datetime.strftime(t, "%Y%m%d%H%M%S")  # s变量里面就是保存的当前时间格式化后的字符串
        oldname = imgurl.name  # 获取的文件的旧的名称 yxrs2.jpg
        pos = oldname.rfind('.')
        extname = ""  # 这个变量用来保存扩展名
        if pos > 0:
            extname = oldname[pos:]  # .jpg把扩展名取出来保存在变量extname中
        fullname = s + extname  # 用当前时间格式化后的字符串与扩展名拼接  得到一个新的文件名20200226144630.jpg
        file_path = os.path.join('static/uploadimg', fullname)  # 拼接出一个完整的路径static/uploadimg\20200226144630.jpg
        file_path = file_path.replace("\\", "/")  # 把路径中的反斜杠替换为斜杠 static/uploadimg/20200226144630.jpg
        with open(file_path, 'wb') as f:
            for chunk in imgurl.chunks():
                f.write(chunk)
    else:  # 没有上传文件的情况
        fullname = ""
    # 图片上传结束

    strsql = "insert into tbroom (proname,price,brief,imgurl) values ('"+tbname+"',"+tbprice+",'"+tbbrief+"','"+fullname+"') "
    cursor.execute(strsql)
    return render(request, 'privateroom.html', {"msg": "保存成功"})

    # 允许在框架下加载



