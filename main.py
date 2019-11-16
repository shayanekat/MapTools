from tkinter import *
import math as Math

def distanceInKmBetweenEarthCoordinates(lat1, lon1, lat2, lon2) :
    earthRadiusKm = 6371

    dLat = Math.radians(lat2-lat1)
    dLon = Math.radians(lon2-lon1)

    lat1 = Math.radians(lat1)
    lat2 = Math.radians(lat2)

    a = Math.sin(dLat/2) * Math.sin(dLat/2) + Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2)
    c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
    return earthRadiusKm * c

def getheading(lat1,lon1,lat2,lon2):
    X = Math.cos(Math.radians(lat2)) * Math.sin(Math.radians(lon2-lon1))
    Y = Math.cos(Math.radians(lat1)) * Math.sin(Math.radians(lat2)) - Math.sin(Math.radians(lat1)) * Math.cos(Math.radians(lat2)) * Math.cos(Math.radians(lon2-lon1))
    return Math.degrees(Math.atan2(X,Y))

def calc():
    lat1 = float(e1.get())
    lon1 = float(e2.get())
    lat2 = float(e3.get())
    lon2 = float(e4.get())
    d = round(distanceInKmBetweenEarthCoordinates(lat1,lon1,lat2,lon2),2)
    h = int(getheading(lat1,lon1,lat2,lon2))
    t3.set("Distance : "+str(d)+"km")
    t4.set("Heading : "+str(h)+"°")

root = Tk()
root.title("MapTools")

l1 = Label(root,text="Point de départ (lat puis long):")
l1.grid(row=0,column=0)

e1 = Entry(root)
e1.grid(row=1,column=0)

e2 = Entry(root)
e2.grid(row=2,column=0)


l2 = Label(root,text="Point d'arrivé (lat puis long) :")
l2.grid(row=0,column=1)

e3 = Entry(root)
e3.grid(row=1,column=1)

e4 = Entry(root)
e4.grid(row=2,column=1)

b = Button(root,text="calculate",command=calc)
b.grid(row=3,column=1)

t3 = StringVar()
l3 = Label(root,textvariable=t3)
l3.grid(row=5,columnspan=2)

t4 = StringVar()
l4 = Label(root,textvariable=t4)
l4.grid(row=6,columnspan=2)

root.mainloop()