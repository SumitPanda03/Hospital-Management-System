import mysql.connector as sql
import getpass
from prettytable import PrettyTable,from_db_cursor
from sys import exit

def about():
    print("This is a project on HOSPITAL MANAGEMENT SYSTEM using Python and MYSQL connection")

def insert_doctor_details():
    print("Enter the deatils of new Doctor")
    d_id=int(input("Enter Doctor id:"))
    d_name=input("Enter Doctor Name:")
    d_age=int(input("Enter Age:"))
    d_department=input("Enter Doctor Department:")
    d_phono=int(input("Enter Phone Number"))
    sql_insert="insert into doctor_details values("""+str(d_id)+",'"+d_name+"',"+str(d_age)+",'"+d_department+"',"+str(d_phono)+")"
    c1.execute(sql_insert)
    print('successfully registered')
    conn.commit()

def show_all_doctor_details():
    sql_x="select d_id as Doctor_ID,d_name as Doctor_Name,d_age as Doctor_Age ,d_department as Doctor_Department,d_phono as Doctor_Phono from doctor_details"
    c1.execute(sql_x)
    #s=c1.fetchall()
    print("                                             ")
    print("All Doctor details are as follows:")
    print("                                             ")
    mytable=from_db_cursor(c1)
    mytable.align="l"
    print(mytable.get_string())
    #for i in s:
        #print(i)


def insert_patient_details():
    print("Enter the deatils of new Patient")
    p_id=int(input("Enter Patient id:"))
    p_name=input("Enter Patient Name:")
    p_age=int(input("Enter Age:"))
    p_problems=input("Enter Patient Problem:")
    p_phono=int(input("Enter Phone Number"))
    sql_insert="insert into patient_details values("""+str(p_id)+",'"+p_name+"',"+str(p_age)+",'"+p_problems+"',"+str(p_phono)+")"
    c1.execute(sql_insert)
    print('successfully registered')
    conn.commit()

def show_all_patient_details():
    sql_w='select p_id as Patient_ID,p_name as Patient_Name,p_age as Patient_Age ,p_problems as Patient_Diagnosis,p_phono as Patient_Phono from patient_details'
    c1.execute(sql_w)
    #r = c1.fetchall()
    print("                                             ")
    print("All Patient details are as follows:")
    print("                                             ")   
    mytable=from_db_cursor(c1)
    mytable.align="l"
    print(mytable.get_string())
    #for i in r :
        #print(i)
        

def insert_worker_details():
    print("Enter the deatils of new Worker")
    w_id=int(input("Enter Worker id:"))
    w_name=input("Enter Worker Name:")
    w_age=int(input("Enter Age:"))
    w_workname=input("Enter Workname:")
    w_phono=int(input("Enter Phone Number:"))
    sql_insert="insert into worker_details values("""+str(w_id)+",'"+w_name+"',"+str(w_age)+",'"+w_workname+"',"+str(w_phono)+")"
    c1.execute(sql_insert)
    print('successfully registered')
    conn.commit()

def show_all_worker_details():
    sql_y="select w_id as Worker_ID,w_name as Worker_Name,w_age as Worker_Age ,w_workname as Worker_Designation,w_phono as Worker_Phono from worker_details;"
    c1.execute(sql_y)
    #t=c1.fetchall()
    print("                                             ")
    print("All Worker details are as follows")
    print("                                             ")
    mytable=from_db_cursor(c1)
    mytable.align="l"
    print(mytable.get_string())
    #for i in t:
        #print(i)

def search_doctor_details():
    print("search Doctor record by entering id")
    sid=int(input("enter doctor id:"))
    sql_d='select * from doctor_details where d_id=("{}")'.format(sid)
    c1.execute(sql_d)
    v=c1.fetchall()
    if len(v) <1:
        print("The Doctor ID does not exist,F")
    else:
        for i in v:
            print(i)


def search_patient_details():
    print("search Patient record by entering id")
    sid=(input("enter patient id:"))
    sql_d='select * from patient_details where p_id=("{}")'.format(sid)
    c1.execute(sql_d)
    v=c1.fetchall()
    if len(v) <1:
        print("Paitent ID does not exist")
    else:
        for i in v:
            print(i)
    
    

def search_worker_details():
    print("search Worker record by entering id")
    sid=int(input("enter worker id:"))
    sql_d='select * from worker_details where w_id=("{}")'.format(sid)
    c1.execute(sql_d)
    v=c1.fetchall()
    if len(v) <1:
        print("The Worker ID does not exist,F")
    else:
        for i in v:
            print(i)
    

def update_doctor_details(d_idn,d_data,d_column):
    
    #update_data=input("Enter new department:")
    #d_id_to_update=int(input("Enter Doctor id:"))
    sql_ub="update doctor_details set "+d_column+" =\'" +d_data+ "\'  where d_id=\'" + d_idn + "\'"
    #print(sql_ub)
    c1.execute(sql_ub)
    print("Data Updated")
    conn.commit()
    
def update_patient_details(p_idn,p_data,p_column):
    
    #update_data=input("Enter new department:")
    #d_id_to_update=int(input("Enter Doctor id:"))
    #sql_u="update patient_details set p_phono ='9123708546' where p_id='410'"
    sql_ux = "update patient_details set "+p_column+" =\'" + p_data + "\' where p_id=\'" + p_idn+ "\'"
    #print(sql_ux)
    c1.execute(sql_ux) 
    print("Data Updated")
    conn.commit()        

def update_worker_details(w_idn,w_data,w_column):
    
    #update_data=input("Enter new department:")
    #d_id_to_update=int(input("Enter Doctor id:"))
    sql_ua="update worker_details set "+w_column+" =\'" +w_data+ "\'  where w_id=\'" +w_idn+ "\'"
    #print(sql_ua)
    c1.execute(sql_ua)
    print("Data Updated")
    conn.commit()        
    

def bill_input():
    try:
        pid=int(input("\n\nEnter the patient ID:"))
        st="select * from patient_details where p_id={}".format(pid)
        c1.execute(st)
        data=c1.fetchall()
        if len(data) <1:
            print("Invalid Patient ID")
        else:
            Roomcost=float(input("Enter the cabin/bed charges (per day):"))
            Days=int(input("Enter the number of days:"))
            Roomcost2=(Roomcost*Days)
            doctor=float(input("Doctor visit charges:"))
            medicine=float(input("Enter the medicine charges:"))
            total=(doctor+medicine+Roomcost2)
            tax=0.18*total
            net=total+tax

            
            from datetime import datetime 
            now1=datetime.now()
            now=now1.strftime("%d/%m/%Y %H:%M")

            print("\n===============GOVERNMENT NURSING HOME===============\n                 INVOICE")
            print("Patient ID:",data[0][0],end ="")
            print("                       ",now)
            print("Name:",data[0][1],end ="")
            print("                    Age:",data[0][2])
            print("Contact No.:",data[0][4])
            print("Illness:",data[0][3])
            print("\n=========_DESCRIPTION_===============",end ="")
            print("_AMOUNT_   ")
            print("Cabin/Bed CHARGES",end ="")
            print("                    ",Roomcost2)
            print("DOCTOR VISIT CHARGES",end ="")
            print("                  ",doctor)
            print("MEDICINES",end ="")
            print("                            ",medicine)
            print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
            print("                           SUB TOTAL:",total)
            print("                            TAX(18%):",tax)
            print("                        TOTAL AMOUNT:",net)
        

    except :
        print("Invalid Input Please Start Again\n\n")
        exit()

conn=sql.connect(host='localhost',user='sonu',passwd='pass1',database='dbtest3')
if conn.is_connected():
      print('successfully connected')
c1=conn.cursor()
x=PrettyTable()

print("----------------------------------------------")
print("1.LOGIN")
print("2.EXIT")
choice=int(input("ENTER YOUR CHOICE:"))
if choice==1:
    
    print("                                                                                                        ")
    print("To have information regarding our hospital please login with the id and password provided at the entrance")
    print("                                                                                                        ")
    u1=input("enter user name:")
    print("                                        ")
    pwd1 = getpass.getpass(prompt="Enter Password: ")
    #pwd1=input("enter the password:")
    if u1=='test' and pwd1=='test1234':
        while u1=='test'and pwd1=='test1234':
            print('connected')
            print("                                                                                       ")

            print('--------------------------------------------------------------')
            print('"                  HOSPITAL MANAGEMENT SYSTEM                "')
            print('--------------------------------------------------------------')
            print("1.About the project")
            print('2.REGISTER DOCTOR DETAILS')
            print('3.ALL DOCTOR DETAILS')
            print('4.REGISTER PATIENT DETAILS')
            print('5.ALL PATIENT DETAILS')
            print('6.REGISTER WORKER DETAILS')
            print('7.ALL WORKER DETAILS')
            print('8.SEARCH DOCTOR DETAILS')
            print('9.SEARCH PATIENT DETAILS')
            print('10.SEARCH WORKER DETAILS')
            print('11.UPDATE DOCTOR DETAILS')
            print('12.UPDATE PATIENT DETAILS')
            print('13.UPDATE WORKER DETAILS')
            print('14.BILL INPUT')          
            print('15.EXIT')
            print('16.Structure')
            print('--------------------------------------------------------------')


            opt=""
            opt=int(input("enter your choice:"))
            if opt==1:
                about()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==2:
                insert_doctor_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==3:
                show_all_doctor_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==4:
                insert_patient_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==5:
                show_all_patient_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==6:
                insert_worker_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==7:
                show_all_worker_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==8:
                search_doctor_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==9:
                search_patient_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==10:
                search_worker_details()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==11:
                doctor_id=input("Enter the doctor id:")
                sql_d='select * from doctor_details where d_id=("{}")'.format(doctor_id)
                c1.execute(sql_d)
                v=c1.fetchall()
                if len(v) <1:
                    print("The Doctor ID does not exist,F")
                else:
                    print("Which column data you want to change")
                    print("1.Doctor_Age")
                    print("2.Doctor_Problem")
                    print("3.Doctor_PhoneNo")

                    
                    choice=""
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        updated_data=input("Enter doctor age:")
                        update_doctor_details(doctor_id,updated_data,'d_age')
                    elif choice==2:
                        updated_data=input("Enter doctor problem:")
                        update_doctor_details(doctor_id,updated_data,'d_department')
                    elif choice==3:
                        updated_data=input("Enter doctor PhoneNo :")
                        update_doctor_details(doctor_id,updated_data,'d_phono')
                    else:
                        print("Option invalid")
                secret_input = getpass.getpass(prompt="Press enter key to continue")
                
            elif opt==12:
                patient_id=input("Enter the patient id:")
                sql_d='select * from patient_details where p_id=("{}")'.format(patient_id)
                c1.execute(sql_d)
                v=c1.fetchall()
                if len(v) <1:
                    print("The Patient ID does not exist,F")
                else:
                    print("Which column data you want to change")
                    print("1.Patient_Age")
                    print("2.Patient_Problem")
                    print("3.Patient_PhoneNo")

                    
                    choice=""
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        updated_data=input("Enter patient age:")
                        update_patient_details(patient_id,updated_data,'p_age')
                    elif choice==2:
                        updated_data=input("Enter patient problem:")
                        update_patient_details(patient_id,updated_data,'p_problems')
                    elif choice==3:
                        updated_data=input("Enter patient PhoneNo :")
                        update_patient_details(patient_id,updated_data,'p_phono')
                    else:
                        print("Option invalid")
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            
            elif opt==13:
                worker_id=input("Enter the worker id:")
                sql_d='select * from worker_details where w_id=("{}")'.format(worker_id)
                c1.execute(sql_d)
                v=c1.fetchall()
                if len(v) <1:
                    print("The Worker ID does not exist,F")
                else:
                    print("Which column data you want to change")
                    print("1.Worker_Age")
                    print("2.Worker_Workname")
                    print("3.Worker_PhoneNo")

                    
                    choice=""
                    choice=int(input("Enter your choice:"))
                    if choice==1:
                        updated_data=input("Enter worker age:")
                        update_patient_details(worker_id,updated_data,'w_age')
                    elif choice==2:
                        updated_data=input("Enter worker problem:")
                        update_patient_details(worker_id,updated_data,'w_problems')
                    elif choice==3:
                        updated_data=input("Enter worker PhoneNo :")
                        update_patient_details(worker_id,updated_data,'w_phono')
                    else:
                        print("Option invalid")
                secret_input = getpass.getpass(prompt="Press enter key to continue")
                
            elif opt==14:
                bill_input()
                secret_input = getpass.getpass(prompt="Press enter key to continue")
            elif opt==15:
                exit()

            elif opt==16:
                c1.execute("DESC doctor_details")
                data=c1.fetchall()
                for field in data:
                    
                    print((field))
                    
                
                break

            else:
                print("INVALID OPTION")
    else:
        print("Wrong User ID or Password")        

if choice==2:
    exit()
