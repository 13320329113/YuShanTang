from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse
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
def getfoodbyid(request):
    id= request.POST.get("id")
    strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where id="+id
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    if row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getfoodlist(request):
    key= request.POST.get("key")
    strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct order by id desc "
    if not key.strip()=="":
        strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct where proname like '%"+key+"%'  order by id desc "
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getfoodlistbyrandom(request):
    strsql = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct order by  RAND() limit 4 "
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def login(request):
    #print("接收到的参数typeid="+str(request.GET.get("typeid")))
    username=request.POST.get("username")
    password = request.POST.get("password")
    print(username)
    print(password)
    strsql="select id,username,password,truename,tel,address from tbmember where username='"+username+"' and password='"+password+"' "
    cursor.execute(strsql)
    conn.commit()
    row = cursor.fetchone()
    s=""
    if row:
        s=str({"id": row[0], "username": row[1], "password": row[2], "truename": row[3], "tel": row[4], "address": row[5]})
        s=s.replace("'","\"")
    res="["+s+"]"
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def reg(request):
    username=request.POST.get("username")
    password = request.POST.get("password")
    tel = request.POST.get("tel")
    address = request.POST.get("address")
    truename = request.POST.get("truename")
    #strsql = "insert into tbusers (username,password,truename,tel,address) values ('"+username+"','"+password+"','"+truename+"','"+tel+"','"+address+"')";
    # cursor.execute(strsql)
    cursor.execute('insert into tbusers (username,password,truename,tel,address) value (%s,%s,%s,%s,%s)',(username,password,truename,tel,address))
    conn.commit()
    s="{\"msg\":\"注册成功\"}"
    res="["+s+"]"
    response=HttpResponse(res)
    response["Access-Control-Allow-Origin"] ="*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def addtocar(request):
    #接收参数
    userid = request.POST.get('userid')
    proid = request.POST.get('proid')
    proname = request.POST.get('proname')
    procount = request.POST.get('procount')
    imgurl = request.POST.get('imgurl')
    price = request.POST.get('price')

    ctime = datetime.datetime.now().strftime('%F %T')
    #我们将一个菜品加入购物车的时候，首先要判断购物车里面是否已经存在这个菜品了，如果已经存在，就增加数量，如果不存在，就插入一条新的记录。
    strsql1="select id from tbshoppingcar where proid="+proid+" and sessionid="+userid
    cursor.execute(strsql1)
    conn.commit()
    row=cursor.fetchone()
    strsql2 = "insert into tbshoppingcar(sessionid,proname,proid,procount,ctime,imgurl,price) values ("+userid+",'"+proname+"',"+proid+","+procount+",'"+ctime+"','"+imgurl+"',"+price+") "
    if row:
        strsql2="update tbshoppingcar set procount=procount+"+procount+" where proid="+proid+" and sessionid="+userid
    print(strsql2)
    cursor.execute(strsql2)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(res)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def getcarlist(request):
    userid= request.POST.get("userid")
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "sessionid": row[1], "proname":row[2], "proid": row[3], "procount": row[4],"ctime": row[5],"imgurl": row[6],"price":str(row[7])})
        row = cursor.fetchone()
    s = str(foodlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

@xframe_options_exempt
def deleteitembyid(request):
    id= request.POST.get("id")
    strsql = "delete from tbshoppingcar where id="+id
    cursor.execute(strsql)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

def changecarnum(request):
    id= request.POST.get("id")
    typeid = request.POST.get("typeid")
    strsql = "update tbshoppingcar set procount=procount+1 where id=" + id
    if typeid=="0":
        strsql = "update tbshoppingcar set procount = IF(procount > 1, procount - 1,1) where id=" + id
    cursor.execute(strsql)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response
#在线下单功能
@xframe_options_exempt
def saveorder(request):
    t = datetime.datetime.now()
    ctime = t.strftime('%Y-%m-%d %H:%M:%S')
    orderid = datetime.datetime.strftime(t, "%Y%m%d%H%M%S%f")
    userid= request.POST.get("userid")
    sumprice = request.POST.get("sumprice")
    sname = request.POST.get("sname")
    stel = request.POST.get("stel")
    saddress = request.POST.get("saddress")
    ptime = request.POST.get("ptime")
    memo = request.POST.get("memo")
    #插入表头信息
    cursor.execute("insert into tborderhead (orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo) values ('"+orderid+"','"+sname+"','"+stel+"','"+saddress+"',"+sumprice+","+userid+",'"+ctime+"','"+ptime+"','"+memo+"')")
    conn.commit()

    #把购物车里面的数据插入到订单明细表
    #先把购物车里当前这个人的菜品查询出来
    strsql = "select id,sessionid,proname,proid,procount,ctime,imgurl,price from tbshoppingcar where sessionid="+userid
    cursor.execute(strsql)
    conn.commit()
    #构造插入订单明细表的sql语句
    sqllists = []
    row = cursor.fetchone()
    while row:
        #{"id": row[0], "sessionid": row[1], "proname": row[2], "proid": row[3], "procount": row[4], "ctime": row[5],"imgurl": row[6], "price": str(row[7])}
        sqllists.append("insert into tborderitems (orderid,proid,proname,price,procount,imgurl) values ('"+orderid+"',"+str(row[3])+",'"+row[2]+"',"+str(row[7])+","+str(row[4])+",'"+row[6]+"')")
        row = cursor.fetchone()
    #遍历sql列表，执行插入订单明细表操作
    for sqlitem in sqllists:
        cursor.execute(sqlitem)
        conn.commit()
    #清空购物车
    cursor.execute("delete from tbshoppingcar where sessionid="+userid)
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

#我的订单
@xframe_options_exempt
def getorderlist(request):
    userid=request.POST.get("userid")
    strsql = "select id,orderid,sname,stel,saddress,sumprice,memberid,ctime,ptime,memo,proname,proid,procount,imgurl,price from v_order where memberid="+userid
    cursor.execute(strsql)
    conn.commit()
    orderlist = []
    row = cursor.fetchone()
    while row:
        orderlist.append({"id": row[0], "orderid": row[1], "sname":str(row[2]), "stel": row[3], "saddress": row[4],"sumprice": str(row[5]),"memberid": row[6],"ctime": row[7],"ptime": row[8],"memo": row[9],"proname": str(row[10]),"proid": row[11],"procount": str(row[12]),"imgurl": row[13],"price": str(row[14])})
        row = cursor.fetchone()
    s = str(orderlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

#在线留言
@xframe_options_exempt
def saveliuyan(request):
    t = datetime.datetime.now()
    ctime = t.strftime('%Y-%m-%d %H:%M:%S')
    username= request.POST.get("username")
    msg1 = request.POST.get("msg1")
    neirong = request.POST.get("neirong")
    #插入表头信息
    cursor.execute("insert into tbliuyan (username,msg1,neirong,ctime) values ('"+username+"','"+msg1+"','"+neirong+"','"+ctime+"')")
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response


#会员注册
@xframe_options_exempt
def register(request):
    #print("接收到的参数typeid="+str(request.GET.get("typeid")))
    username=request.POST.get("username")
    password = request.POST.get("password")
    truename = request.POST.get("truename")
    tel = request.POST.get("tel")
    address = request.POST.get("address")
    print(username)
    print(password)
    print(truename)
    print(tel)
    print(address)
    cursor.execute("insert into tbmember (username,password,truename,tel,address) values ('"+username+"','"+password+"','"+truename+"','"+tel+"','"+address+"')")
    conn.commit()
    s = "{\"msg\":\"ok\"}"
    res = "[" + s + "]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response

#酒水饮料
@xframe_options_exempt
def getdrinklist(request):
    key= request.POST.get("key")
    strsql1 = "select id,proname,price,imgurl from tbdrink where type =1 order by id desc "
    cursor.execute(strsql1)
    conn.commit()
    drinklist1 = []
    row = cursor.fetchone()
    while row:
        drinklist1.append({"id": row[0], "proname": row[1], "price":str(row[2]), "imgurl": row[3]})
        row = cursor.fetchone()
    s1 = str(drinklist1)
    s1 = s1.replace("'", "\"")

    strsql2 = "select id,proname,price,imgurl from tbdrink where type =2 order by id desc "
    cursor.execute(strsql2)
    conn.commit()
    drinklist2 = []
    row = cursor.fetchone()
    while row:
        drinklist2.append(
            {"id": row[0], "proname": row[1], "price":str(row[2]), "imgurl": row[3]})
        row = cursor.fetchone()
    s2 = str(drinklist2)
    s2 = s2.replace("'", "\"")

    strsql3 = "select id,proname,price,imgurl from tbdrink where type =3 order by id desc "
    cursor.execute(strsql3)
    conn.commit()
    drinklist3 = []
    row = cursor.fetchone()
    while row:
        drinklist3.append({"id": row[0], "proname": row[1], "price":str(row[2]), "imgurl": row[3]})
        row = cursor.fetchone()
    s3 = str(drinklist3)
    s3 = s3.replace("'", "\"")

    strsql4 = "select id,proname,price,imgurl from tbdrink where type =4 order by id desc "
    cursor.execute(strsql4)
    conn.commit()
    drinklist4 = []
    row = cursor.fetchone()
    while row:
        drinklist4.append({"id": row[0], "proname": row[1], "price":str(row[2]), "imgurl": row[3]})
        row = cursor.fetchone()
    s4 = str(drinklist4)
    s4 = s4.replace("'", "\"")

    s = "["
    s += "{"
    s += " \"id\":\"1\","
    s += " \"typename\":\"饮料\","
    s += "\"prolist\":"
    s += s1
    s += " },"
    s += "{"
    s += "\"id\":\"2\","
    s += " \"typename\":\"啤酒\","
    s += "\"prolist\":"
    s += s2
    s += "},"
    s += " {"
    s += "\"id\":\"3\","
    s += " \"typename\":\"白酒\","
    s += "\"prolist\":"
    s += s3
    s += " },"
    s += "{"
    s += " \"id\":\"4\","
    s += " \"typename\":\"红酒\","
    s += "\"prolist\":"
    s += s4
    s += "}]"
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response



@xframe_options_exempt
def getcooklist(request):
    # key= request.POST.get("key")
    strsql = "select id,imgurl,cookname,cookdescribe,cooklable from cookerlist order by id desc "
    # if not key.strip()=="":
    #     strsql = "select id,imgurl,cookname,cookdescribe,cooklable from cookerlist where cookname like '%"+key+"%'  order by id desc "
    cursor.execute(strsql)
    conn.commit()
    cooklist = []
    row = cursor.fetchone()
    while row:
        cooklist.append({"id": row[0], "imgurl": row[1], "cookname":str(row[2]), "cookdescribe": row[3], "cooklable": row[4]})
        row = cursor.fetchone()
    s = str(cooklist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response




@xframe_options_exempt
def getlunbolistbyrandom(request):
    strsql = "select id,imgurl from lunboimg order by  RAND() limit 4 "
    cursor.execute(strsql)
    conn.commit()
    lunbolist = []
    row = cursor.fetchone()
    while row:
        lunbolist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    s = str(lunbolist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response




@xframe_options_exempt
def getroomlist(request):
    key= request.POST.get("key")
    strsql = "select id,proname,price,brief,imgurl from tbroom order by id desc "
    if not key.strip()=="":
        strsql = "select id,proname,price,brief,imgurl from tbroom where proname like '%"+key+"%'  order by id desc "
    cursor.execute(strsql)
    conn.commit()
    roomlist = []
    row = cursor.fetchone()
    while row:
        roomlist.append({"id": row[0], "proname": row[1], "price": str(row[2]), "brief": row[3], "imgurl": row[4]})
        row = cursor.fetchone()
    s = str(roomlist)
    s = s.replace("'", "\"")
    response = HttpResponse(s)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response



@xframe_options_exempt
def getdatalistbyrandom(request):
    strsql1 = "select id,proname,price,brief,descriptions,istop,isstar,imgurl,typeid from tbproduct order by  RAND() limit 4 "
    cursor.execute(strsql1)
    conn.commit()
    foodlist = []
    row = cursor.fetchone()
    while row:
        foodlist.append({"id": row[0], "proname": row[1], "price":str(row[2]), "brief": row[3], "descriptions": row[4],"istop": row[5],"isstar": row[6],"imgurl": row[7],"typeid": row[8]})
        row = cursor.fetchone()
    s1 = str(foodlist)
    s1 = s1.replace("'", "\"")

    strsql2 = "select id,cookname,imgurl from cookerlist order by RAND() limit 3"
    cursor.execute(strsql2)
    conn.commit()
    cookerlist = []
    row = cursor.fetchone()
    while row:
        cookerlist.append({"id": row[0], "cookname": row[1], "imgurl": row[2]})
        row = cursor.fetchone()
    s2 = str(cookerlist)
    s2 = s2.replace("'", "\"")

    strsql3 = "select id,imgurl from lunboimg order by  RAND() limit 3 "
    cursor.execute(strsql3)
    conn.commit()
    pptlist = []
    row = cursor.fetchone()
    while row:
        pptlist.append({"id": row[0], "imgurl": row[1]})
        row = cursor.fetchone()
    s3 = str(pptlist)
    s3 = s3.replace("'", "\"")
    s0 = "[{\"foodlist\":" + s1 + ",\"cookerlist\":" + s2 + ",\"pptlist\":" + s3 + "}]"

    response = HttpResponse(s0)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    response["Access-Control-Allow-Methods"] = "DELETE, PUT, POST"
    return response




