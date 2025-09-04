# take the input of temperature in celsius

a = int(input("Enter the temperature :"))

if a < 0 :
        print("Freezing cold")
elif a >= 0 and a<10 :
        print("Very Cold")
elif a >= 10 and a<20 :      
        print("Cold")  
elif a >= 20 and a<30 :        
        print("Pleasant")
elif a >= 30 and a< 40 :    
        print("Hot")    
else :        
        print("Very Hot")