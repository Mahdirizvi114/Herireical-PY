print("_____________________________________Welcome To Our Showroom________________________________________")
print()
print()
class Cars:
    Car1= "Toyota Supra"
    fuel1= "13 KM/LTR"
    License1= "All Documents Are Clear"

    car2="ford Mustang"
    fuel2= "15 KM/LTR"
    License2= "Registration Is Remaining."

    def printdata_Cars_Details(self):
        print(f'''Hey How Are You? Iam The Manager Here. We offers You Some Cars So Please Come With Me
               
              I'll Show You. Here Is The Lastest Model Of {self.Car1} With Fuel Efficiency Of {self.fuel1} 

              and the Registration of {self.License1} And Another Car As You Can See Is That {self.car2}

              With Fuel Efficiency Of {self.fuel2} And All Document Are Clear Only {self.License2}''')
        
        print()
        print()
class Bikes(Cars):

    Bike1= "Kawasaki h2r"
    Fuel1= "30 KM/LTR"
    license1= "Just Sit And Enjoy The Ride"

    Bike2= "Honda S1000"
    Fuel2= "35 KM/LTR"
    license2= "All Documents Are Setted up Just Need To Be Registered."

    def printdata_Bikes_Details(self):
        print(f'''Dear Valuable Customer As You Can See That Our Showroom Provide Serives Of Bike Along With
              
              Cars So Here Iam Going To Show You That What Types Of Bike Are Avaliable Here. The First Bike

              Which you Can See That It Is {self.Bike1} Its is The Most Powerful Bike With Fuel Average Of

               {self.Fuel1} And Their Is No Need for Any Registration {self.license1}. We Also Have Another Bike In

                Our Collection Which Is {self.Bike2} It Is Also The Powerful Machine With Fuel Average Of

                 {self.Fuel2} But If We Look At The Document Side That {self.license2} ''')
        
        print()
        print()

class Trucks(Bikes):
    truck1= "Toyota Revo"
    fuell1= "25 KM/LTR"
    Registration1="Are All Okay."

    truck2= "Lamborghini Urus"
    fuell2= "22 KM/LTR"
    Registration2="We Don't Provide Registration Service."

    def printdata_Truck_Details(self):
        print(f'''We Have Started The Business Of Trucks With The Colab Of These Companies. One Is {self.truck1}
               
With Fuel Average of {self.fuell1} And The documents {self.Registration1} And Second is {self.truck2} With Fuel

Average Of {self.fuell2} And We Are Sorry To Say That {self.Registration2}''')        
        


object1= Cars()
object2=Bikes()
object3= Trucks()

object3.printdata_Cars_Details()
object3.printdata_Bikes_Details()
object3.printdata_Truck_Details()
print()
print()
print("-------------------------------------------------------------------------------------------------------")
print("____________________________________________HAPPY TO SEE YOU___________________________________________")
print("-------------------------------------------------------------------------------------------------------")

        


