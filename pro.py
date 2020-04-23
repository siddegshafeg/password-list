import os

def fun2(x,y):
    array1 = ["123","1234","12345","12345678","13456789","12456789","12356789","12346789","12345789","12345689","12345679","2012","2013","lol","2014","2015","2016","2017","2018","2019","1999","2000","2001","2002","2020","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","12344321","123321","123456789","13456789","12456789","12356789","12346789","12345789","12345689","12345679","87654321","lil","wiz","mo","big","cr7","Cr7","CR7"," ","\"","ex","EX","Ex"]
    
    for l in array1 :
        A   = x+y
        A1  = l+x+y
        A2  = x+l+y
        A4  = x+y+l 
        D2  = y+l+x
        E2  = l+y+x
        E3  = y+l+x
        E4  = y+x+l
        F2  = y+l+x      
        c1  = x
        c13 = l+x
        c14 = x+l     
        g1  = x+x
        g11 = l+x+x
        g12 = x+l+x
        g14 = x+x+l
        h12 = l+x+x
        h13 = x+l+x
        h14 = x+x+l
        a21 = l+x+y
        a22 = x+l+y
        a23 = x+y+l
        b22 = l+y
        b23 = y+l#------------
        c2  = y
        f2  = y+y
        f21 = l+y+y
        f22 = y+l+y
        f23 = y+y+l
        
         
        rr.write(A+"\n")
        rr.write(A1+"\n")
        rr.write(A2+"\n"+ D2+"\n"+ E2+"\n"+ F2+"\n")
        rr.write(E3+"\n")
        rr.write(A4+"\n"+ E4+"\n")
             

        rr.write(c1+"\n"+c2+"\n"+f2+"\n"+g1+"\n")
             
        rr.write(a21+"\n"+f21+"\n"+g11+"\n")
        rr.write(a22+"\n"+b22+"\n"+f22+"\n"+g12+"\n")
        rr.write(a23+"\n"+b23+"\n"+c13+"\n"+f23+"\n"+h13+"\n")
        rr.write(     c14+"\n"+g14+"\n"+h14+"\n")






def fun3(x,y):
     
     array = ["@","!","_","#","$","&","*","+","?","%","-","\""," ",","]
     array1 = ["123","1234","12345","12345678","13456789","12456789","12356789","12346789","12345789","12345689","12345679","2012","2013","2014","2015","2016","2017","2018","2019","2020"]
     for z in array :
         for l in array1 :
             A = x+z+y
             A1 = l+x+z+y
             A2 = x+l+z+y
             A3 = x+z+l+y
             A4 = x+z+y+l
         
             B  =  z+x+y
             B1 = z+l+x+y
             B2 = z+x+l+y
             B3 = z+x+y+l
             B4 = l+z+x+y
         
             C  = x+y+z
             C1 = l+x+y+z
             C2 = x+l+y+z
             C3 = x+y+l+z
             C4 = x+y+z+l
         
             D = y+z+x
             D1 = l+y+z+x
             D2= y+l+z+x
             D3 = y+z+l+x
             D4 = y+z+x+l
         
             E = z+y+x
             E1 = l+z+y+x
             E2 = z+l+y+x
             E3 = z+y+l+x
             E4 = z+y+x+l
         
             F = y+x+z
             F1 = l+y+x+z
             F2 = y+l+x+z
             F3 = y+x+l+z
             F4 = y+x+z+l
         
             a1 = x+z
             a11 = l+x+z
             a12= x+l+z
             a13 = x+z+l#------------
    
         
        
             b1 = z+x
             b11 = l+z+x
             b12 = z+l+x
             b13 = z+x+l#------------
            
             c1 = z+z+x
             c11 = l+z+z+x
             c12 = z+l+z+x
             c13 = z+z+l+x
             c14 = z+z+x+l
             
             d1 = z+x+z
             d11 = l+z+x+z
             d12 = z+l+x+z
             d13 = z+x+l+z
             d14 = z+x+z+l
         
             e1 = x+z+z
             e11 = l+x+z+z
             e12 = x+l+z+z
             e13 = x+z+l+z
             e14 = x+z+z+l
         
             f1 = x+x+z
             f11 = x+x+z
             f12 = x+x+z
             f13 = x+x+z
             f14 = x+x+z
             
             g1 = x+z+x
             g11 = l+x+z+x
             g12 = x+l+z+x
             g13 = x+z+l+x
             g14 = x+z+x+l
         
             h1 = z+x+x
             h11 = l+z+x+x
             h12= z+l+x+x
             h13 = z+x+l+x
             h14 = z+x+x+l

             a2 = x+y+z
             a21 = l+x+y+z
             a22 = x+l+y+z
             a23 = x+y+l+z
             a24= x+y+z+l
 
             b2 = z+y
             b21 = l+z+y
             b22 = z+l+y
             b23 = z+y+l#------------

             c2 = z+z+y
             c21 = l+z+z+y
             c22 = z+l+z+y
             c23 = z+z+l+y
             c24 = z+z+y+l

             d2 = z+y+z
             d21 = l+z+y+z
             d22 = z+l+y+z
             d23 = z+y+l+z
             d24 = z+y+z+l

             e2 = y+z+z
             e21 = l+y+z+z
             e22 = y+l+z+z
             e23 = y+z+l+z
             e24 = y+z+z+l

             f2 = y+y+z
             f21 = l+y+y+z
             f22 = y+l+y+z
             f23 = y+y+l+z
             f24 = y+y+z+l

             g2 = y+z+y
             g21 = l+y+z+y
             g22 = y+l+z+y
             g23 = y+z+l+y
             g24 = y+z+y+l

             h2 = z+y+y
             h21 = l+z+y+y
             h22 = z+l+y+y
             h23 = z+y+l+y
             h24 = z+y+y+l
         
             rr.write(A+"\n"+B+"\n"+C+"\n"+ D+"\n"+ E+"\n"+ F+"\n")
             rr.write(A1+"\n"+B1+"\n"+C1+"\n"+ D1+"\n"+ E1+"\n"+ F1+"\n")
             rr.write(A2+"\n"+B2+"\n"+C2+"\n"+ D2+"\n"+ E2+"\n"+ F2+"\n")
             rr.write(A3+"\n"+B3+"\n"+C3+"\n"+ D3+"\n"+ E3+"\n"+ F3+"\n")
             rr.write(A4+"\n"+B4+"\n"+C4+"\n"+ D4+"\n"+ E4+"\n"+ F4+"\n")
             

             rr.write(a1+"\n"+a2+"\n"+b1+"\n"+b2+"\n"+c1+"\n"+c2+"\n"+d1+"\n"+d2+"\n"+e1+"\n"+e2+"\n"+f1+"\n"+f2+"\n"+g1+"\n"+g2+"\n"+h1+"\n"+h2+"\n")
             
             rr.write(a11+"\n"+a21+"\n"+b11+"\n"+b21+"\n"+c11+"\n"+c21+"\n"+d11+"\n"+d21+"\n"+e11+"\n"+e21+"\n"+f11+"\n"+f21+"\n"+g11+"\n"+g21+"\n"+h11+"\n"+h21+"\n")
             rr.write(a12+"\n"+a22+"\n"+b12+"\n"+b22+"\n"+c12+"\n"+c22+"\n"+d12+"\n"+d22+"\n"+e12+"\n"+e22+"\n"+f12+"\n"+f22+"\n"+g12+"\n"+g22+"\n"+h12+"\n"+h22+"\n")
             rr.write(a13+"\n"+a23+"\n"+b13+"\n"+b23+"\n"+c13+"\n"+c23+"\n"+d13+"\n"+d23+"\n"+e13+"\n"+e23+"\n"+f13+"\n"+f23+"\n"+g13+"\n"+g23+"\n"+h13+"\n"+h23+"\n")
             rr.write(         a24                  +"\n"+c14+"\n"+c24+"\n"+d14+"\n"+d24+"\n"+e14+"\n"+e24+"\n"+f14+"\n"+f24+"\n"+g14+"\n"+g24+"\n"+h14+"\n"+h24+"\n")
       
             
   
        
            
        
os.system("clear")
print("{______________ THIS IS TOOL FOR PASSWORD LIST_____________}")
print("")









M = input("ENTER THE NAME OF THE FILE (PASSWORD LIST)  : ")
rr = open(M,"a")

name        =  input("Enter the NAME :  "          )
nikname     =  input("Enter the NIKNAME :  "       )
age         =  input("Enteer the AGE : "           )
barthday    =  input("Ender the BARTHDAY    : "   )
phonenumber =  input("Enter the PHONE NUMBER : "   )
fname       =  input("Enter the FATHER NAME : "   )
mname       =  input("Enter the MOTHER NAME  : "   )
gps         =  input("Etnter LOCATION make it simple :")
date        =  input("Enter  spical  date like Date marriage:")
thing       =  input("Enter  favorite  color : ")
apet        =  input("Enter favorite animal:")
gp          =  input("Enter the Favorite person like  Boyfriend or Girlfriend : ")
print ("DONE! (pleas please wait)")
#-------------------------------------------------------------------------------------
name1        =  name.upper()
nikname1     =  nikname.upper()
age1         =  age.upper()
barthday1    =  barthday.upper()
phonenumber1 =  phonenumber.upper()
fname1       =  fname.upper()
mname1       =  mname.upper()
gps1         =  gps.upper()
date1        =  date.upper()
thing1       =  thing.upper()
apet1        = apet.upper()
gp1          =  gp.upper()
#-------------------------------------------------------------------------------------

name2        =  name.capitalize()
nikname2     =  nikname.capitalize()
age2        =  age.capitalize()
barthday2    =  barthday.capitalize()
phonenumber2 =  phonenumber.capitalize()
fname2      =  fname.capitalize()
mname2       =  mname.capitalize()
gps2         =  gps.capitalize()
date2       =  date.capitalize()
thing2       =  thing.capitalize()
apet2         = apet.capitalize()
gp2          =gp.capitalize()

#--------------------------------------------------------------------------------------


h =  [name,nikname,age,barthday,phonenumber,fname,mname,gps,date,thing,apet,gp]
h1 = [name1,nikname1,age1,barthday1,phonenumber1,fname1,mname1,gps1,date1,thing1,apet1,gp1]
h2 = [name2,nikname2,age2,barthday2,phonenumber2,fname2,mname2,gps2,date2,thing2,apet2,gp2]
for a in h:
    for a1  in h:
        fun2(a,a1)
        fun3(a,a1)
        for b in h1:
            fun2(a,b)
            fun3(a,b)

for r in h1:   
    for m in h2:
        fun2(r,m)
        fun3(r,m)

for c in h:   
    for b in h2:
        fun2(c,b)
        fun3(c,b)

for q in h1:
    for z in h1:
        fun2(q,z)
        fun3(q,z) 

for p in h2:
    for x in h2:
        fun2(p,x)
        fun3(p,x) 


    




        


rr.close()

