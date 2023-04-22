def bill_input():
    try:
        pid=int(input("\n\nEnter the patient ID:"))
        st="select * from patient_details where p_id={}".format(pid)
        cursor.execute(st)
        data=cursor.fetchall()
        #The error for wrong P_id should appear here...But it appears after few steps though
        Roomcost=float(input("Enter the cabin/bed charges (per day):"))
        Days=int(input("Enter the number of days:"))
        Roomcost2=(Roomcost*Days)
        doctor=float(input("Doctor visit charges:"))
        medicine=float(input("Enter the medicine charges:"))
        total=(doctor+medicine+Roomcost2)
        tax=0.18*total
        net=total+tax

        ans=str(input("Do you want to generate Bill? (Y/N):"))
        from datetime import datetime 
        now1=datetime.now()
        now=now1.strftime("%d/%m/%Y %H:%M")
        if ans=='Y':
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
            print("                           SUB TOTAL:",total)
            print("                            TAX(18%):",tax)
            print("                        TOTAL AMOUNT:",net)
        else:
            2*aaaa
    except :
        print("Invalid Input Please Start Again\n\n")
        bill_input()