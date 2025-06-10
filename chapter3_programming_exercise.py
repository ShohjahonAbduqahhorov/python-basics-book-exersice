## 1
##Ask the user to enter a number and find the number obtained by reversing the order of the digits
#a=int(input("Enter a number \t:"))
#if a<=9999 and a>=1000:
#    q=a%10
 #   w=(int(a/10)%10)
 #   e=(int(a/100)%10)
#    r=(int(a/1000)%10)
 #   a1=q*1000+w*100+e*10+r
 #   print("The number that obtained by reversing the given number is ",a1)
#elif a<=999 and a>=100:
 #   q=a%10
#    w=(int(a/10)%10)
 #   e=(int(a/100)%10)
 #   a1=q*100+w*10+e
#    print("The number that obtained by reversing the given number is ",a1)
#elif a<=99 and a>=10:
  #  q=a%10
  #  w=(int(a/10)%10)
  #  a1=q*10+w
   # print("The number that obtained by reversing the given number is ",a1)
#elif a<10 and a>=0:
#    print("Please enter a bit greater number")
#elif a<0 :
 #   print("Please enter a positive number")
#else:
   # print("Please enter a number which is less than 9999")
   
   
 ## 2
 ## Ask the user to enter a four digit number and check whether the sum of the \
     ## first and the last digits is same as the sum of the second and the third digits
#num=int(input("Enter a four digit number \t:"))
#a=num%10
#b=(int(num/10))%10
#c=(int(num/100))%10
#d=(int(num/1000))%10
#if a+d==b+c :
#    print(" The sum of the first and the last digits is same as the sum of the second and the third digits")
#else :
 #   print("The sum of the first and the last digits is not same as the sum of the second and the third digits")
    
   
## 3
## In the above question if the answer is true then obtain a number in whivh the second and the third\
    ## digits are one more than that in the given number
#num=int(input("Enter a four digit number \t:"))
#a=num%10
#b=(int(num/10))%10
#c=(int(num/100))%10
#d=(int(num/1000))%10
#if a+d==b+c :
  #  print(" The sum of the first and the last digits is same as the sum of the second and the third digits")
#    b1=b+1
  #  c1=c+1
  #  num1=d*1000+c1*100+b1*10+a
  #  print("New number :",num1)
#else :
#    print("The sum of the first and the last digits is not same as the sum of the second and the third digits")



## 4.5.6
## Ask the user to enter the concentration of hydrogen ions in a given solution (c) \
    ## and find the PH of the solution using the following formula.
    ## PH=log10(C)
#c=float(input("Enter the concentration of hydrogen ions (C) \t:"))
#import math
#ph=math.log10(c)
#print("PH=",ph)
#if ph<7 :
#    print("The solution is deemed acidic")
#elif ph==7:
#    print("The solution is neutral")
#else:
 #   print("The solution is deemed basic")
 
 
 
    ## 7
## The centripetal force acting on a body (mass m ),moving with velocity v ,
##in a circle of radius r, is given by the formula m*v^2/r.The gravitational force
## on the body is given by the formula (GmM)/R^2,where m and M are the masses of bodyu and earth 
## and R is the radius of the earth.Ask the user to enter the requisite data 
## and find whether the two forces are equal or not.
#v=float(input("Enter the velocity \t:"))
#r=float(input("Enter the radius of a circle \t:"))
#m=float(input("Enter the mass of a body"))
#from scipy.constants import G 
#mass_earth=5.9722e24
#radius_earth=6.371e6
#a=m*(v**2)/r
#b=(G*m*mass_earth)/(radius_earth)**2
#if a ==b:
 #   print("These two forces are equal")
#else:
 #   print("These two forces are not equal")
 
 
 
 ## 8
 ## Ask the user to enter his salary and calculate the TATA,which is 10% of \
     ## the salary; the HRA which is 20% of the salary and the gros income, which \
         ## is the sum total of the salary,TADA and the HRA
#salary=float(input("Enter your salary \t:"))
#t=salary/10
#h=salary/5
#g=t+h
#("the TADA =",t)
#print("the HRA=",h)
#print("the gross income=",g)



## 11
## Find whether a number entered by the user is divisible by 3 and 13
#a=float(input("Enter a number \n>>>"))
#b=a%3
#if b==0:
 #   print("The number is divisible by 3")
#else :
  #  print("The number is not divisible by 3")
#c=a%13
#if c==0:
 #   print("The number is divisible by 13")
#else: 
  #  print("The number is not divisible by 13")

    
    
    
## 12
## Find whether the number enterd by the user is perfect square.
#a=int(input("Enter a number \t:"))
#import math
#b=math.sqrt(a)
#c=b-math.floor(b)
#if c==0:
 #   print("The number is perfect square")
#else :
 #   print("The number is not perfect square")


    
    
    
    
    
    
    
    
    
    
    
    
    
    
