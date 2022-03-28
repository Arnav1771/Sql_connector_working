import mysql.connector
from tabulate import tabulate
mydb=mysql.connector.connect(host="localhost",user="root",password="Bandarjai123")
mycursor=mydb.cursor()
sql="CREATE DATABASE if not exists magb"
mycursor.execute(sql)
mycursor=mydb.cursor()
mycursor.execute("use customer1")
query ="""CREATE TABLE IF NOT EXISTS ORDERS(SNO int,CUSTOMER_NAME varchar(250),ITEM_NAME varchar(20),ITEM_TYPE varchar(50),QUANTITY int,PRICE int,SCHARGE float,TAX float,AMOUNT float,NET_AMOUNT float)""" 
mycursor.execute(query)
while True:
  print('\n\n\n')
  print("*"*90)
  print('\t\t\t\t\tMAIN MENU')
  print("*"*90)
  print('\t\t\t\t\t1.Adding item record')
  print('\t\t\t\t\t2.Display all record')
  print('\t\t\t\t\t3.Deleting all records')
  print('\t\t\t\t\t4.Deleting particular item records')
  print('\t\t\t\t\t5.Display items records on roll')
  print('\t\t\t\t\t6.Display records of particular item')
  print('\t\t\t\t\t7.Update Record')
  print('\t\t\t\t\t7.Exit')
  ch=int(input("enter your choice: "))
  if ch==1:
    try:
      mycursor.execute=mydb.cursor
      print('enter item details')
      SNO=int(input("enter serial no. "))
      INAME=input("enter item name ")
      ITYPE=input("enter item type - soft drink/combo/burger ")
      QUAN=int(input("enter item quantity "))
      PRICE=int(input("enter price "))
      NAME=input("Enter Customer Name ")
      if QUAN==1: 
        SCHARGE=PRICE*0.5*QUAN
        TAX=PRICE*0.4
      elif QUAN==2:
        SCHARGE=PRICE*0.4*QUAN
        TAX=PRICE*0.3
      else:
        SCHARGE=PRICE*0.3*QUAN
        TAX=PRICE*0.2
      AMOUNT=PRICE+SCHARGE
      NET_AMOUNT=AMOUNT+TAX
      rec = (SNO,NAME,INAME,ITYPE,QUAN,PRICE,SCHARGE,TAX,AMOUNT,NET_AMOUNT)
      query = "insert into orders values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      mycursor=mydb.cursor()
      mycursor.execute(query,rec)
      mydb.commit()
      print("recorded added successfully....")
    except Exception as e:
      print("something went wrong",e)
  elif ch==2:
    try:
      query= "select * from orders"
      mycursor.execute(query)
      print(tabulate(mycursor, headers=['SNO','CUSTOMER_NAME','ITEM_NAME','ITEM_TYPE','QUANTITY','PRICE','SCHARGE','TAX','AMOUNT','NET_AMOUNT'],tablefmt='psql'))
    except Exception as e:
      print("something went wrong",e)
  elif ch==3:
    try:
      ch=input("do you want to delete all ther records ")
      if ch.upper()=="Y":
        mycursor.execute("delete from orders")
        mydb.commit()
        print("all the records deleted ")
    except Exception as e:
      print("something went wrong",e)
  elif ch==4:
    try:
      an=input("enter sno of item to delete")
      query="delete from orders where SNO ="+an
      mycursor.execute(query)
      print("Record Deleted")
    except Exception as e:
     print("something went wrong",e)
      
  elif ch==5:
    try:
      query="select * from orders"
      mycursor.execute(query)
      myrecords=mycursor.fetchall()
      print("/n/n/")
      print(90*"")
      print("itempayroll".center(80))
      print(90*"")
      print("%-5s%-5s%-15s%-10s%-8s%-8s%-8s%-8s%-9s%-8s"%('SNO','CUSTOMER_NAME','ITEM_NAME','ITEM_TYPE','QUANTITY','PRICE','SCHARGE','TAX','AMOUNT','NET_AMOUNT'))
      print(80*"-")
      for rec in myrecords:
        print("%-4d %-15s%-15s %-10s %-8.3f %-8.3f %-8.2f %-9.2f %-8.2f %-9.2f "%rec)
        print(90*"-")
    except Exception as e:
      print("somthing went wrong",e)


  elif ch==6:
    try:
      an=input("enter sno whose payslip is to retrive")
      query="select * from orders where SNO ="+an
      mycursor.execute(query) 
      print(tabulate(mycursor, headers=['SNO','ITEM_NAME','ITEM_TYPE','OUANTITY','PRICE','SCHARGE','TAX','AMOUNT','NET_AMOUNT'],tablefmt='psql'))
    except Exception as e:
     print("something went wrong",e)
  elif ch==7:
    try:
      ch=int(input("\n1.ITEM_NAME \n2.ITEM_TYPE \n3.QUANTITY \n4.CUSTOMER NAME \n Enter Field to be update = "))
      if ch==1:
        an=input("Enter Name To be update ")
        sn=int(input("Enter SNO "))
        query="UPDATE orders SET ITEM_NAME = %s WHERE SNO = %s"
        mycursor.execute(query,(an,sn))
        print("Updated Successfully")
      elif ch==2:
        an=input("Enter Item Type To be update ")
        sn=int(input("Enter SNO "))
        query="UPDATE orders SET ITEM_TYPE = %s WHERE SNO = %s"
        mycursor.execute(query,(an,sn))
        print("Updated Successfully")
      elif ch==3:
        an=input("Enter Quantity To be update ")
        sn=int(input("Enter SNO "))
        query="UPDATE orders SET QUANTITY = %s WHERE SNO = %s"
        mycursor.execute(query,(an,sn))
        print("Updated Successfully")
      elif ch==4:
        an=input("Enter Customer Name To be update ")
        sn=int(input("Enter SNO "))
        query="UPDATE orders SET CUSTOMER_NAME = %s WHERE SNO = %s"
        mycursor.execute(query,(an,sn))
        print("Updated Successfully")
      else:
        print("Wrong Input")
    except Exception as e:
     print("something went wrong",e)
  elif ch==8:
    break
    print("Exit Successfully")
else:
  print("wrong choice:")
2