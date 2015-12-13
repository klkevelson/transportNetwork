__author__ = 'lchau17'

# Town part
import time
from datetime import date

class people:
    def __init__(self,pVehicle,name):
        self.pVehicle= pVehicle
        self.name = name

    def getName(self):
        return self.name
    def pVehicle(self):
        return self.pVehicle
    pass


class Town:
    def __init__(self,Tag,startTown, endTown,distance): # Town has its Tag,startTown, endTown adn distance
        self.TownName = Tag # set same for the
        self.startTown = startTown
        self.endTown = endTown
        self.distance = None

    def getName(self):
        return self.TownName
    def getStart(self):
        return self.startTown
    def getDistance(self):
        return self.distance

    def getEnd(self):
        return self.endTown



    def __str__(self):
        return self.TownName


#build town(s)


class Vehicles:
    def __init__(self, wheel, driver, color,speed, fuel ,number,capacity):
        self.wheel = wheel
        self.driver = driver
        self.color = color
        self.speed = speed
        self.fuel = fuel
        self.vehiclesNumber = number
        self.capacity = capacity


    def setWheel(self):
        return self.wheel
    def setdriver(self):
        return self.driver
    def setColor(self):
        return self.color
    def SetSpeed(self):
        return self.speed
    def setFuel(self):
        return self.fuel
    def setNumber(self):
        return self.vehiclesNumber
    def setCapacity(self):
        return self.capacity


    def __str__(self):
        texting = " The vhicles have " + str(self.wheel) + " wheel(s)"
        texting +=" The driver is " + self.driver
        texting += "The color is " + self. color
        texting += "The speed is " + str(self. speed)
        return texting


class Bus(Vehicles):
    def __init__(self,wheel, driver, color,speed,fuel,number,capacity,size ):
        super(Bus,self).__init__(wheel, driver, color,speed,fuel ,number,capacity)
        self.busSize = size

    def getSize(self):
        return self.busSize


    def __str__(self):
        busOutPut = "Bus's Number: " + str(self.vehiclesNumber) +"\n"
        busOutPut += "Bus's Color: " +str(self.color)+"\n"
        busOutPut += "Dirver: " + str(self.driver) + "\n"
        busOutPut += "\n"+str(temp) + " gets ON the bus \n"

        return busOutPut


class Car(Vehicles):
    def __init__(self,wheel, driver, color,speed,fuel,number, capacity,brand):
        super(Car,self).__init__(wheel, driver, color,speed,fuel ,number,capacity)
        self.carBrand = brand


    def __str__(self):
        pass

# Build Car # Car0 & Car1
Car0 = Car(4,"Eason","black", 120, 90,"A123",5, "Jeep")
Car1 = Car(4,"Jack"," white", 200,81,"B123", 7, "Toyota")




class Taxi(Vehicles):
    def __init__(self,wheel, driver, color,speed,fuel,number, capacity):
        super(Taxi,self).__init__(wheel, driver, color,speed,fuel ,number,capacity)

    def __str__(self):
        taxiOutPut = "Taxi's Number: " + str(self.vehiclesNumber) +"\n"
        taxiOutPut += "Taxi's Color: " +str(self.color)+"\n"
        taxiOutPut += "Dirver: " + str(self.driver) + "\n"
        taxiOutPut += "\n"+str(temp) + " gets ON the Taxi \n"

        return taxiOutPut


    __repr__ = __str__




class Trains(Vehicles):
    def __init__(self,wheel, driver, color,speed,fuel,number, capacity):
        super(Trains,self).__init__(wheel, driver, color,speed,fuel ,number,capacity)

    def __str__(self):
        pass


class Bicycles(Vehicles):
    def __init__(self,wheel, driver, color,speed,fuel,number, capacity,distance, ):
        super(Bicycles,self).__init__(wheel, driver, color,speed,fuel ,number,capacity,distance)
    def __str__(self):
        pass

class Aircraft(Vehicles):
    def __init__(self,wheel, driver, color,speed,fuel,number, capacity,distance,):
        super(Aircraft,self).__init__(wheel, driver, color,speed,fuel ,number,capacity,distance)
    def __str__(self):
        pass







def addPeople():

    temp = input("Please enter the passenger's name")

    choiceGO_line = input("There are 6 options (Type the # ONLY)"+
                        "\n\tOption 1 : Long Island--> Washington, D.C\n\t"+
                          "Option 2 : Long Island--> Boston\n\t"+
                          "Option 3 : Boston --> Washington, D.C\n\t"+
                          "Option 4 : Boston --> Long Island\n\t"+
                          "Option 5 : Washington, D.C --> Boston\n\t"+
                          "Option 6 : Washington, D.C --> Long Island\n\t")

    if choiceGO_line  == 1 :
        Town.getDistance("")
        getBus = Bus1
        getTaxi= Taxi0
        busCost = "$46"

    elif choiceGO_line  == 2 :
        Town.getDistance (292)
        getBus = Bus2
        getTaxi = Taxi1
        busCost = "$100"
    elif choiceGO_line  == 3 :
        Town.getDistance (706)
        getBus = Bus3
        getTaxi = Taxi2
        busCost =" $80"
    elif choiceGO_line  == 4 :
        Town.getDistance (292)
        getBus = Bus4
        getTaxi = Taxi3
        busCost =" $100"
    elif choiceGO_line  == 5 :
        Town.getDistance (706)
        getBus = Bus5
        getTaxi = Taxi4
        busCost =" $80"
    else:
        Town.getDistance (453)
        busCost = "$46"
        getBus = Bus6
        getTaxi = Taxi5

    chooseTransportation = input("Please choose a transportaiton \n"+
                                 "(bus,car,taxi,trains,bicycles,or aircraft) :")

    # the bus part
    if chooseTransportation == "bus":
        print("Price :" +str(busCost))
        print(str(getBus))
        time.sleep(2)
        print(str(temp) + " gets OFF the bus")

        #Bus Carbon Footprint

        BusCarbonFootprint = int(Town.getDistance) * 0.3 * 0.785
        RoundBCF = round(BusCarbonFootprint,2)
        print("Bus's Carbon Footprint: " + str(RoundCF) +" Kg")
        AmountPlantingTree = (float(BusCarbonFootprint) //78.5)
        print(str(temp) +" needs to plant " + str(AmountPlantingTree)+
              " tree(s) for compensating the environment. ")
        return RoundBCF
    # the taxi part
    elif chooseTransportation == "taxi":
        TaxiCost = int(Town.getDistance) * 1.26 + 2.5
        RoundTC = round(TaxiCost,2)
        print("Price : ＄" +str(TaxiCost))
        print(str(getTaxi))
        time.sleep(2)
        print(str(temp) + " gets OFF the taxi")
        #Taxi Carbon Footprint
        TaxiCarbonFootprint = int(Town.getDistance) * 0.1 * 0.785
        RoundTCF = round(TaxiCarbonFootprint,2)
        print("Bus's Carbon Footprint: " + str(RoundTCF) +" Kg")
        AmountPlantingTree = (float(TaxiCarbonFootprint) //78.5)
        print(str(temp) +" needs to plant " + str(AmountPlantingTree)+
              " tree(s) for compensating the environment. ")
        return RoundTC
    else:
        print("Thank you")



def main():

    #Building Town and Bus; trying to let them work together
    Town0= Town("Town A","A", "B", 360 )
    Town1= Town("Town B","B", "C",580 )
    Town2 = Town("Town C", "A", "C",240 )
    Town3= Town("Town D", "B", "C", 240)
    return (Town0,Town1,Town2,Town3) 

def main1():
    # Set 6 Buses for three citys
    Bus1 = Bus(4,"Jack","blue ", 110,80, 1, "Huge" ,100)
    Bus2 = Bus(4,"Andy","yellow ",110,80, 2, "Huge" ,100)
    Bus3 = Bus(4,"Summer ","black ",110,80, 3, "Huge" ,100)
    Bus4 = Bus(4,"Andy","white ",100,80, 4, "Huge" ,100)
    Bus5 = Bus(4,"Joe","red ",110,80, 5, "Huge" ,100)
    Bus6= Bus(4,"Brain","gray",110,80, 6, "Huge" ,100)
    return (Bus1,Bus2,Bus3,Bus4,Bus5,Bus6)
    
def main2():
    # Set 6 Taxi for three citys
    Taxi0 = Taxi(4,"Sam","Yellow",120, 94, "T123", 5, )
    Taxi1 = Taxi(4,"Peter","black",120, 94, "T123", 5, )
    Taxi2 = Taxi(4,"Levi","blue",120, 94, "T123", 5, )
    Taxi3 = Taxi(4,"Jocab","gray",120, 94, "T123", 5, )
    Taxi4 = Taxi(4,"David","white",120, 94, "T123", 5, )
    Taxi5 = Taxi(4,"Eillen","red",120, 94, "T123", 5, )
    return (Taxi0,Taxi1,Taxi2,Taxi2,Taxi3,Taxi4,Taxi5)
def main3():

    #Set 6 trains for three citys
    Train1 = Trains(50,"Jack","gray ", 200,80, 0 ,100)
    Train2 = Trains(50,"Colin","gold ", 200,80, 1 ,100)
    Train3 = Trains(50,"August","white ", 200,80, 1 ,100)
    Train4 = Trains(50,"Charlie","blue ", 200,80, 1 ,100)
    Train5 = Trains(50,"Cystal","red ", 200,80, 1 ,100)
    Train6 = Trains(50,"Emily","yellow  ", 200,80, 1 ,100)
    return (Train1,Train2,Train3,Train4,Train5,Train6)


print("\nHey, welcome to LeukKwan Chau's Transport Network ;)\n\t ")
print("Today is " + str(date.today())+"\n\t")

main()
main1()
main2()
main3()
#addPeople()

check = Town.getDistance(0)
print(check)
