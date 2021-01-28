print("1-Future Value\t \n2-present Value\t \n3-present value of Annuity\t\n4-Future Value of annuity\t\n5-Effective Annual Rate\t\n6-value of perpetuity")
x = int(input("Enter your Choice: "))
if x == 1:
   pv = int(input("Enter present value:"))
   i = int(input("Enter Interest Rate:"))
   year = int(input("Enter Years:"))
   i = i/100
   Fv = pv*((1 + i)**year)
   print("Future value is:", Fv)
elif x == 2:
    Fv = int(input("Enter Future value:"))
    i = int(input("Enter Interest Rate:"))
    year = int(input("Enter Years:"))
    i = i / 100
    pv = Fv / ((1 + i) ** year)
    print("Future value is:", pv)
elif x == 3:
    print("1-ordinary Annuity\t2-Due Annuity")
    x = int(input("Enter Choice:"))
    if x == 1:
       '''present value of ordinary annuity'''
       pmt = int(input("Enter payment:"))
       i = int(input("Enter interest Rate:"))
       i = i/100
       year = int(input("Enter years:"))
       PVA = (pmt / i)*(1-(1 / ((1 + i) ** year)))
       print("present value of Annuity is:", PVA)
    elif x == 2:
          '''present value od annuity due'''
          pmt = int(input("Enter payment:"))
          i = int(input("Enter interest Rate:"))
          i = i / 100
          year = int(input("Enter years:"))
          pva = (pmt / i) * (1 - (1 / ((1 + i) ** year)) * (1+i))
          print("present value of Annuity is:", pva)
    else:
         print("Sorry!\nYou enter invalid number")
elif x == 4:
        print("1-ordinary Annuity\t2-Due Annuity")
        x = int(input("Enter Choice:"))
        if x == 1:
             #future value of ordinary annuity
             pmt = int(input("Enter payment:"))
             i = int(input("Enter interest Rate:"))
             i = i / 100
             year = int(input("Enter years:"))
             fva = (pmt / i) * ( ( (1 + i) ** year )-1)
             print("Future value of ordinary Annuity is:", fva)
        elif x == 2:
             # future value od annuity due
             pmt = int(input("Enter payment:"))
             i = int(input("Enter interest Rate:"))
             i = i / 100
             year = int(input("Enter years:"))
             fva = (pmt / i) * ( ( (1 + i) ** year )-1) * (1+i)
             print("Future value of Annuity Due is:", fva)
elif x == 5:
     i = int(input("Enter Interest:"))
     m = int(input("Enter compounding rate:"))
     ear=((1+(i/m))**m)-1
     print("Effective Annual Rate is:", ear)
elif x == 6:
     pmt = int(input("Enter payment:"))
     i = int(input("enter interest rate:"))
     per = pmt / i
     print("Value of perpetuity",  per)
else:
    print("sorry!\nyou enter invalid number:")