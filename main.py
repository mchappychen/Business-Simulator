""" 
 ___     ___   _         _  	           _____   _       ____   _       _____
|   \   /   | |_|  ___  | |      _____    |  __ | | |     |  __| | |     |  __ |  ______
| |\ \_/ /| |  _  |  _| | |___  |  _  |   |  ___| | |     | |    | |___  |  ___| \   _  |
| | \___/ | | | | | |_  |  _  | | |_| |_  | |___  | |     | |__  |  _  | | |___   | | | |
|_|       |_| |_| |___| |_| |_| |_______| |_____| |_|     |____| |_| |_| |_____|  |_| |_|     
 Fixed Input Cost Market Simulation
 Date: 1/31/17
 Period:1
 """

from graphics import *
import random
import time
class Window:
    def __init__(self):
        self.x = 800
        self.y = 600
        self.day = 0
        self.textSize = 25
        self.accountBalance = 0
        self.revenue = 0   #Revenue
        self.stock = 0  #Quanity owned
        self.inputCost = 0 #Input Cost
        self.profit = self.revenue - self.inputCost #Profit
        self.name = "" #User's name
        self.product = ""
        self.price = 0 #Price of the product
        self.xIntercept = 0 #For Demand Curve
        self.yIntercept = 0
        #[Title,text,demand-shift]
        self.cakeNews = [   #I placed the list of news here so that its changes can be preserved
            ["CAKES ARE UNHEALTHY","The University of Antarctica has\nfound a shocking discovery on\nthe strong correlation between cakes and\ndiabetes. \'They have too much\nsugar, the public should really refrain\nfrom eating them\' says Dr. Michael,\nthe leading scientist in this study.",-20],
            ["POLICE SHOOTING SPARKS\nPROTESTS","An amateur video shot by a\nbystander, officer Repucci fatally shot an\nunarmed 9 year old girl while she was\nmaking cake. Protesters are encouraging\neveryone to buy cakes to support their\ncampaign in prosecuting Repucci.",50],
            ["NATIONAL CAKE DAY","The President of the United States has\nofficial declared this day to be National\nCake Day. Citizens world-wide are\ncelebrating by buying more cake.",200],
            ]
        self.carNews = [
            ["MITSUBISHI OPENS UP\nSTORES","The foreign company, Mitsubishi, has\nopened their ever-popular shop at the\nother side of town. Hurry up and\nget there to get the cheapest prices!\nSorry to the other car firms that have\nto compete with Mitusbishi.\nMay you rest in peace.",-40],
            ["ECONOMY BOOST","Statisticians have estimated a\nlarge increase in the incomes of\nmany Americans. \'I am delighted\nby this shift\' says economist \nDr. David. \'I expect an increase in purchases\nof expensive products like cars.\'",20],
            ["SEVERE WEATHER\nDESTROYS PARKING LOT","Severe thunderstorms were blamed for\nthe destruction of a university's parking\nlot. Investigators say that large hail\ndamaged the cars, which leaked gasoline,\nand a struck of lightning lit the\nfloor on fire.",5], 
            ]
        self.gasNews = [
            ["BOYCOTT "+self.name.upper()+"!",self.name+"'s oil rig exploded over the Gulf\nof Mexico, prompting ocean wildlife\nprotestors to boycott their gas.",0],
            ["BP DROPS OUT","The massive company, BP, has\nofficially announced on twitter that\n they're going out of business. \'That's\none less competitor for the gas\n industry\' says economist Rempala.",20],
            ["RISE IN ELECTRIC CARS","People are starting to use\nelectric cars more than \ngas-powered cars.",-10],
            ["NEW AMUSEMENT PARK BUILT","As part of the mayor\'s\n initiative to attract more\nvisitors to town, the new amusement\n park will bring in more travelers.",20]
            ]
        self.newsList = [self.cakeNews,self.carNews,self.gasNews]
        
    def createInterface(self): #makes the window and divides the sections with lines
        self.win = GraphWin("Window",self.x,self.y)
        self.line1 = Line(Point(self.x//2,self.y),Point(self.x//2,0))
        self.line2 = Line(Point(self.x//2,self.y//2),Point(self.x,self.y//2))
        self.line3 = Line(Point(0,self.y//6),Point(self.x//2,self.y//6))
        self.line4 = Line(Point(0,self.y//3),Point(self.x//2,self.y//3))
        self.line5 = Line(Point(0,self.y//2),Point(self.x//2,self.y//2))
        self.line6 = Line(Point(0,(self.y*2)//3),Point(self.x//2,(self.y*2)//3))
        self.line7 = Line(Point(0,(self.y*5)//6),Point(self.x//2,(self.y*5)//6))
        self.line1.draw(self.win)  #Drawing the lines to organize/separate the sections
        self.line2.draw(self.win)
        self.line3.draw(self.win)
        self.line4.draw(self.win)
        self.line5.draw(self.win)
        self.line6.draw(self.win)
        self.line7.draw(self.win)
        self.textDay = Text(Point(self.x//4,self.y//12),self.name+"'s "+self.product+" shop. Day "+str(self.day)) #setting texts
        self.textDay.setSize(self.textSize)
        self.textDay.draw(self.win)
        self.textAccountBalance = Text(Point((self.x//4)+30,self.y//4),"Account Balance: $"+str(self.accountBalance))
        self.textAccountBalance.setSize(self.textSize)
        self.textAccountBalance.draw(self.win)
        self.textStock = Text(Point(self.x//4,(self.y*5)//12),"Capital Stock: "+str(self.stock))
        self.textStock.setSize(self.textSize)
        self.textStock.draw(self.win)
        self.textRevenue = Text(Point(self.x//4,(self.y*7)//12),"Revenue: "+str(self.revenue))
        self.textRevenue.setSize(self.textSize)
        self.textRevenue.draw(self.win)
        self.textInputCost = Text(Point(self.x//4,(self.y*3)//4),"Input Cost "+str(self.inputCost))
        self.textInputCost.setSize(self.textSize)
        self.textInputCost.draw(self.win)
        self.textProfit = Text(Point(self.x//4,(self.y*11)//12),"Profit: "+str(self.revenue - self.inputCost))
        self.textProfit.setSize(self.textSize)
        self.textProfit.draw(self.win)
        self.newsText = Text(Point((self.x*3)//4,(self.y*9)//16),"News")
        self.newsText.setSize(26)
        self.newsText.draw(self.win)
        
    def getProduct(self): #ask the user for product to sell
        product = button("Gas, Car, or Cake?",17)
        if product.lower() == "cake" or product.lower() == "car" or product.lower() == "gas":   
            self.product = product
            return product
        return self.getProduct()
    
    def setGraph(self): #create curve based on elasticity
        self.graph = Rectangle(Point((self.x*9)//16,(self.y)//16),Point((self.x*15)//16,(self.y*7)//16))
        self.graph.draw(self.win)
        self.demandCurve = Line(Point((self.x*9)//16,self.y//8),Point((self.x*27)//32,(self.y*7)//16))
        self.demandCurve.setWidth(2)
        self.demandCurve.draw(self.win)
        self.xMidPoint = ((self.demandCurve.getP2().getX() - self.demandCurve.getP1().getX())//2) + self.demandCurve.getP1().getX()
        self.yMidPoint = ((self.demandCurve.getP2().getY() - self.demandCurve.getP1().getY())//2) + self.demandCurve.getP1().getY()
        self.maxRevenue = Circle(Point(self.xMidPoint,self.yMidPoint),3)
        self.maxRevenue.setFill("Black")
        self.xMaxRevenueLine = Line(Point((self.x*9)//16,self.yMidPoint),Point(self.xMidPoint,self.yMidPoint))
        self.yMaxRevenueLine = Line(Point(self.xMidPoint,self.yMidPoint),Point(self.xMidPoint,(self.y*7)//16))
        self.maxRevenue.draw(self.win)
        self.xMaxRevenueLine.draw(self.win)
        self.yMaxRevenueLine.draw(self.win)
        self.demandText = Text(Point((self.x*26)//32,(self.y*5)//16),"Demand Curve")
        self.demandText.draw(self.win)
        self.graphTitle = Text(Point((self.x*24)//32,self.y//32),"Aggregate Demand Graph")
        self.graphTitle.setSize(self.textSize)
        self.graphTitle.draw(self.win)
        self.yAxis = Text(Point((self.x*17)//32,(self.y)//4),"Price")
        self.yAxis.draw(self.win)
        self.xAxis = Text(Point((self.x*12)//16,(self.y*15)//32),"Quantity")
        self.xAxis.draw(self.win)
        
    def setAccountBalance(self,product):
        if product.lower() == "car":
            self.accountBalance = 100000
        elif product.lower() == "cake":
            self.accountBalance = 5000
        elif product.lower() == "gas":
            self.accountBalance = 20000
        
    def getNews(self, product):  #gets random news
        if self.day == 1:
            return ["NEW STORE IN\nTOWN","A new store named "+self.name+"\'s "+self.product+"\nshop is opened for the first day.\nLet\'s see how smart they are!",0]
        nonews = random.random()
        if nonews > 0.3: #No news happening
            return ["","",0]
        #BEGIN ABSTRACTION:
        x = 0
        if product.lower() == "cake":
            x = 0
        elif product.lower() == "car":
            x = 1
        elif product.lower() == "gas":
            x = 2
        if len(self.newsList[x])==0:
            return ["","",0]
        selector = random.randint(0,len(self.newsList[x])-1)
        theNews = self.newsList[x][selector]
        self.newsList[x].remove(theNews)
        return theNews


    def setNews(self,product):
        self.newsBox = Rectangle(Point((self.x*9)//16,(self.y*19)//32),Point((self.x*15)//16,(self.y*15)//16))
        self.newsBox.draw(self.win)
        self.newsTitle = Text(Point((self.x*3)//4,(self.y*11)//16),product[0])
        self.newsTitle.setSize(20)
        self.newsTitle.draw(self.win)
        self.newsBody = Text(Point((self.x*3)//4,(self.y*13)//16),product[1])
        self.newsBody.setSize(15)
        self.newsBody.draw(self.win)

    def setCost(self,product,quantityBought):
        if product.lower() == "gas":
            self.inputCost = 4 * quantityBought
        elif product.lower() == "cake":
            self.inputCost = 3 * quantityBought
        elif product.lower() == "car":
            self.inputCost = 5000 * quantityBought
        self.textInputCost.undraw()
        self.textInputCost = Text(Point(self.x//4,(self.y*3)//4),"Total Cost: "+str(self.inputCost))
        self.textInputCost.setSize(self.textSize)
        self.textInputCost.draw(self.win)
        
    def start(self,product,w): #Starts from Day 1, asks for price, then calculates revenue based on graph
        self.day += 1
        self.setDay()
        news = w.getNews(product)
        w.setNews(news)
        self.win.setBackground(color_rgb(random.randint(1,255),random.randint(1,255),random.randint(1,255)))
        self.setCost(product,1)
        self.setBalance()
        self.setIntercepts()
        self.setCurve()
        self.buy()
        self.getPrice()
        pass #Gets Revenue
        self.setProfit()
        time.sleep(5)
        self.newsTitle.undraw()
        self.newsBody.undraw()

    def setIntercepts(self):
        if self.product.lower() == "cake":
            self.xIntercept = 40
            self.yIntercept = 27
        if self.product.lower() == "car":
            self.xIntercept = 5
            self.yIntercept = 9000
        if self.product.lower() == "gas":
            self.xIntercept = 1000
            self.yIntercept = 5
        
    def setCurve(self):
        # SETS CURVE POSITIONS BASED ON PRODUCT USING IFs
        #shift the intercepts by demand
        self.xInterceptText = Text(Point(self.demandCurve.getP2().getX(),(self.y*15)//32),"("+str(self.xIntercept)+", 0)")
        self.xInterceptText.draw(self.win)
        self.yInterceptText = Text(Point((self.x*17)//32,self.demandCurve.getP1().getY()),"(0, "+str(self.yIntercept)+")")
        self.yInterceptText.draw(self.win)
        self.textMidLine = Text(Point(self.xMidPoint+20,self.yMidPoint-10),"("+str(self.xIntercept//2)+", "+str(self.yIntercept//2)+")")
        self.textMidLine.draw(self.win)
        """
        1. Make an equation
        y = -ax + b
        price (-1*slope*x) + self.yIntercept
        slope = self.yIntercept//self.xIntercept
        price = (-1*(self.yIntercept//self.xIntercept)*Q) + self.yIntercept
        
        Since we're putting PRICE as input, we need to find the INVERSE of the equation

        Quantity = ((self.price - self.yIntercept) * self.xIntercept)//(-1*self.yIntercept) = Quantity
        Revenue = Price * Quantity
        """
    
    def getPrice(self):
        self.price = int(button("Name your Price"))

    def setProfit(self):
        self.textProfit.undraw()
        self.textProfit = Text(Point(self.x//4,(self.y*11)//12),"Profit: "+str(self.revenue - self.inputCost))
        self.textProfit.setSize(self.textSize)
        self.textProfit.draw(self.win)
    
    def getName(self):
        self.name = button("Name")

    def setDay(self):
        self.textDay.undraw()
        self.textDay = Text(Point(self.x//4,self.y//12),self.name+"'s "+self.product+" shop. Day "+str(self.day)) #setting texts
        self.textDay.setSize(self.textSize)
        self.textDay.draw(self.win)
        
    def setBalance(self):
        self.textAccountBalance.undraw()
        print(self.accountBalance)
        self.textAccountBalance = Text(Point((self.x//4)+30,self.y//4),"Account Balance: $"+str(self.accountBalance))
        self.textAccountBalance.setSize(self.textSize)
        self.textAccountBalance.draw(self.win)

    def setStock(self):
        self.textStock.undraw()
        self.textStock = Text(Point(self.x//4,(self.y*5)//12),"Capital Stock: "+str(self.stock))
        self.textStock.setSize(self.textSize)
        self.textStock.draw(self.win)
        
    def buy(self):
        quantityBought = int(button("Input Cost is "+str(self.inputCost)+" Per Unit. How much do you want to buy?",12))
        if quantityBought * self.inputCost <= self.accountBalance:
            self.accountBalance -= self.inputCost * quantityBought
            self.stock = quantityBought
            self.setBalance()
            self.setStock()
            self.setCost(self.product,quantityBought)
        else:
            print("Not enough money")
            self.buy()
    

def button(text,textSize=24): #I Used ABSTRACTION to make a button with a flexible text for input
        w = GraphWin("",300,200)
        TEXT = Text(Point(150,30),text)
        TEXT.setSize(textSize)
        TEXT.draw(w)
        e = Entry(Point(150,75),20)
        e.setSize(20)
        e.draw(w)
        button = Rectangle(Point(100,110),Point(200,150))
        button.setFill("Cyan") #Making a submit button
        button.draw(w)
        textSubmit = Text(Point(150,130),"Submit")
        textSubmit.setSize(15)
        textSubmit.draw(w)
        a = True
        Input = ""
        while(a):
            b = w.getMouse() #Event for if the mouse is clicked in the rectangle
            if b.getX()<200 and b.getX()>100 and b.getY() >110 and b.getY()<150:
                a = False
                Input = e.getText()
        w.close()    
        return Input

def main():
    w = Window()
    w.getName()
    product = w.getProduct()
    w.setAccountBalance(w.product)
    w.createInterface() 
    w.setGraph()
    w.start(product,w)

main()
