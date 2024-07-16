from django.shortcuts import render
import mysql.connector


def home(request):
    return render(request, "home.html")


def aboutus(request):
    return render(request, "aboutus.html")


def feedback(request):
    return render(request, "feedback.html")


# Create your views here.

def bookaction(request):
    name = request.POST['name']
    email = request.POST['email']
    age = request.POST['age']
    contact = request.POST['contact']
    department = request.POST['department']
    consultant = request.POST['consultant']
    date = request.POST['date']
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="test", port="3306")
    operations = con.cursor()
    sql = ("insert into hpappointment(appname,appemail,appage,appcontact,appdepartment,appconsultant,appdate) "
           "values(%s,%s,%s,%s,%s,%s,%s)")
    values = (name, email, age, contact, department, consultant, date)
    operations.execute(sql, values)
    con.commit()
    con.close()
    return render(request, "home.html")


def addfeedback(request):
    feed_name = request.POST['feed_name']
    feed_email = request.POST['feed_email']
    feed_desc = request.POST['feed_desc']
    feed_rating = request.POST['rating']
    con = mysql.connector.connect(host="localhost", user="root", password="root", database="test", port="3306")
    operations = con.cursor()
    sql = "insert into hpfeedback(feedname,feedemail,feedrating,feeddesc) values(%s,%s,%s,%s)"
    values = (feed_name, feed_email, feed_rating, feed_desc)
    operations.execute(sql, values)
    con.commit()
    return render(request, "feedback.html")

def authoritypage(request):
    return render(request,"authority.html")
