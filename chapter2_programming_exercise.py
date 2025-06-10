## 1. Write a program to swap two numbers.
#a=int(input("Enter the first number: \n>>>"))
#b=int(input("Enter the second number: \n>>>"))
#print("The numbers entered are ",a,'and',b)
#print("The numbers are now",b,"and",a)


## 2.Ask the user to enter the coordinates of a point 
## and find the distance of the the point from the origin
#x=float(input("Enter the x coordinate of the point \n>>>"))
#y=float(input("Enter the y coordinate of the point \n>>>"))
#d=x**2+y**2
#import math
#distance=math.sqrt(d)
#print("The distance of the point from the origin is ",distance)
 

## 3. Ask the user to enter two points(x and y coordinates) 
## and find the distance between them.
#x1=float(input("Enter the x coordinate of the first point \n>>>"))
#y1=float(input("Enter the y coordinate of the first point \n>>>"))
#x2=float(input("Enter the x coordinate of the second point \n>>>"))
#y2=float(input("Enter the y coordinate of the second point \n>>>"))
#d=(x1-x2)**2+(y1-y2)**2
#import math
#distance=math.sqrt(d)
#print("The distance between these two points is ",distance)


## 4. Ask the user to enter three points and find whether they are collinear
#print("Enter coordinates of three points:")
#x1= float(input("Enter the x coordinate of the first point : "))
#y1 = float(input(" Enter the y coordinate of the first point : "))
#x2= float(input(" Enter the x coordinate of the second point : "))
#y2= float(input(" Enter the y coordinate of the second point : "))
#x3= float(input(" Enter the x coordinate of the third point :"))
#y3= float(input(" Enter the y coordinate of the third point : "))
#a=(x1-x2)**2+(y1-y2)**2
#b=(x2-x3)**2+(y2-y3)**2
#c=(x1-x3)**2+(y1-y3)**2
#import math
#a1=math.sqrt(a)
#a2=math.sqrt(b)
#a3=math.sqrt(c)
#p=(a1+a2+a3)/2
#s=math.sqrt(p*(p-a1)*(p-a2)*(p-a3))
#if s==0 :
#     print("They are collinear")
#else :
#    print("They are not collinear")


## 5.6 In the above question , if these points are not collinear, find the type of the triangle formed by the points
#x1= float(input("Enter the x coordinate of the first point : "))
#y1 = float(input(" Enter the y coordinate of the first point : "))
#x2= float(input(" Enter the x coordinate of the second point : "))
#y2= float(input(" Enter the y coordinate of the second point : "))
#x3= float(input(" Enter the x coordinate of the third point :"))
#y3= float(input(" Enter the y coordinate of the third point : "))
#a=(x1-x2)**2+(y1-y2)**2
#b=(x2-x3)**2+(y2-y3)**2
#c=(x1-x3)**2+(y1-y3)**2
#import math
#a1=math.sqrt(a)
#a2=math.sqrt(b)
#a3=math.sqrt(c)
#p=(a1+a2+a3)/2
#s=math.sqrt(p*(p-a1)*(p-a2)*(p-a3))
#if s==0 :
 #   print("They are collinear")
#else :
  #  print("They are not collinear")
 #   if a1==a2 and a2==a3:
#        print("The triangle made of these points is equilateral")
#    elif a1==a2 or a2==a3 or a1==a3:
#        print("The triangle made of these points is isosceles")
 #   else :
 #        print("The triangle made of these points is scalene")
 #        if a+b==c or a+c==b or b+c==a :
 #            print("This is right triangle")
 #        else:
  #           print("This is not right triangle")


## 8.Ask the user to enter two points and find if they are at equal distances from the origin   
#x1= float(input("Enter the x coordinate of the first point : "))
#y1 = float(input(" Enter the y coordinate of the first point : "))
#x2= float(input(" Enter the x coordinate of the second point : "))
#y2= float(input(" Enter the y coordinate of the second point : "))
#a =x1**2+y1**2
#b=x2**2+y2**2
#if a==b :
#    print("They are at equal distance from the origin")
#else:
 #   print("They are not at equal distance from the origin")
    


## 9
## In question number 8, find the angle between the line joining the points and the origin
x1= float(input("Enter the x coordinate of the first point : "))
y1 = float(input(" Enter the y coordinate of the first point : "))
x2= float(input(" Enter the x coordinate of the second point : "))
y2= float(input(" Enter the y coordinate of the second point : "))
a =x1**2+y1**2
b=x2**2+y2**2
c=(x1-x2)**2+(y1-y2)**2
x=(a+b-c)/(2*a*b)
import math
angle_rad=math.acos(x)
angle_deg=math.degrees(angle_rad)
print("The angle between the line joining the points and the origin is ",angle_deg)


 
 

