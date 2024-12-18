import os
os.system("cls")

cars = [
    {
        "make": "audi",
        "model": "R8",
        "year": 2023,
        "colors": ["blue", "green", "daytona gray"],
        "hp": 700
    },
    {
        "make": "ferrari",
        "model": "458",
        "year": 2003,
        "colors": ["blue", "green", "daytona gray"],
        "hp": 800
    },
    {
        "make": "lamborghini",
        "model": "reuvelto",
        "year": 2020,
        "colors": ["blue", "green", "daytona gray"],
        "hp": 900
    }
]




while True:
    for car in cars:
        make = car["make"]
        model = car["model"]
        hp = car["hp"]
        print(f"{make} {model} med {hp} hästkrafter")
        
    position = input("vilken bil vill du ta bort? 0. (först)  1. (mellan)  2. (sista)")
    
    cars.pop(int(position))
        

    
    