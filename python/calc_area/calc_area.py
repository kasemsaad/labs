shape = input("enter shape name ")
def calc_area(shape,width,height):
    f1=open("result.txt",'w')
    if shape=="squ":
        width =eval(input("enter width "))
        res=width*width
        f1.write("square length  = "+str(height)+" area = "+str(res))
    elif(shape=="rec"):
        width = eval(input("enter width "))
        height = eval(input("enter height "))
        res=height*width
        f1.write("rectangle hight  = " + str(height) + " rectangle width = " + str(width)+" area = "+ str(res))
    elif(shape=="cir"):
        pi=3.14
        width=eval(input("enter radius "))
        res=pi*width*width
        f1.write("circle  radius = " + str(width) + " area = " + str(res))
    elif(shape=="tri"):
        width =eval(input("enter buttom "))
        height =eval(input("enter height "))
        res=0.5*height*width
        f1.write("triangle buttom  = " + str(width) + "triangle height = "+str(height)+ " area = " + str(res))


calc_area(shape,width=0,height=0)