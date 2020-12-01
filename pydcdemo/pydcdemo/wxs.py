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

@xframe_options_exempt
def cookeraddpost(request):

    #接收参数
    cookname = request.POST.get('cookname')
    cookdes = request.POST.get('cookdes')
    cooklable = request.POST.getlist('cooklable')


    print(str(cooklable))

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
    aa="  ".join(cooklable)
    strsql = "insert into cookerlist (imgurl,cookname,cookdescribe,cooklable) values ('"+fullname+"','"+cookname+"','"+cookdes+"','"+aa+"')"
    cursor.execute(strsql)
    return render(request, 'cooklistadd.html',{"msg":"保存成功"})


@xframe_options_exempt
def cooklistadd(request):
 return render(request, 'cooklistadd.html')

@xframe_options_exempt
def cooklist(request):
    strsql = "select id,imgurl,cookname,cookdescribe,cooklable from cookerlist order by id desc"
    cursor.execute(strsql)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    cooklist=[]
    while row:
        #print(row)
        cooklist.append({"id": row[0], "imgurl": row[1], "cookname": row[2],"cookdescribe": row[3],"cooklable": row[4]})
        row = cursor.fetchone()
        print()
    return render(request, 'cooklist.html',{'cooklist': cooklist})

@xframe_options_exempt
def cookedit(request):
    id = request.GET.get("id")
    strsql1 = "select id,imgurl,cookname,cookdescribe,cooklable  from cookerlist where id="+id
    cursor.execute(strsql1)
    row = cursor.fetchone()
    view={"id": row[0], "imgurl": row[1], "cookname": row[2],"cookdescribe": row[3],"cooklable": row[4]}
    return render(request, 'cookedit.html',{'cookview': view})

#上传菜品图片
@xframe_options_exempt
def cookeditpost(request):
    #接收参数
    proid = request.POST.get("proid")
    oldimgurl = request.POST.get("oldimgurl")

    imgurl = request.FILES.get("imgurl")
    cookname = request.POST.get("cookname")
    cookdescribe = request.POST.get("cookdescribe")
    cooklable = request.POST.getlist("cooklable")



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

    aa="  ".join(cooklable)
    print(aa)
    sqlstr = "update cookerlist set imgurl='"+fullname+"',cookname='"+cookname+"',cookdescribe='"+cookdescribe+"',cooklable='"+aa+"' where id="+proid
    cursor.execute(sqlstr)
    conn.commit()
    view = {"id": proid,  "imgurl": fullname,"cookname": cookname, "cookdescribe": cookdescribe, "cooklable": cooklable,
            "address":"","msg":"保存成功"}
    return render(request, 'cookedit.html',{'cookview': view})

@xframe_options_exempt
def cookdelete(request):
    #删除数据
    id = request.GET.get("id")
    sqlstr1="delete from cookerlist where id="+id
    cursor.execute(sqlstr1)
    conn.commit()
    #重新查询数据，渲染列表模板
    sqlstr2 = "select id,imgurl,cookname,cookdescribe,cooklable from cookerlist order by id desc"
    cursor.execute(sqlstr2)  # 此行代码执行查询语句，把查询的结果保存在cursor对象中
    row = cursor.fetchone()
    cooklist = []
    while row:
        # print(row)
        cooklist.append({"id": row[0], "imgurl": row[1], "cookname": row[2], "cookdescribe": row[3], "cooklable": row[4]})
        row = cursor.fetchone()
    return render(request, 'cooklist.html', {'cooklist': cooklist})

