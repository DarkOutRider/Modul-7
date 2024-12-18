#dectionary är en datastruktur som anges i nyckel:värde-par
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

#print(cars[0]["make"])
#cars[0]["hp"] = 1000



#print(cars["make"], cars ["model"], cars["year"])
"""
for car in cars:
    make = cars["make"]
    model = cars["model"]
    year = cars["year"]

print(f"du har en {make} {model} från {year}")

make = cars[1]["make"]
model = cars[1]["model"]
year = cars[1]["year"]

print(f"du har en {make} {model} från {year}")

make = cars[2]["make"]
model = cars[2]["model"]
year = cars[2]["year"]

print(f"du har en {make} {model} från {year}")"""



while True:
    for car in cars:
        make = car["make"]
        model = car["model"]
        hp = car["hp"]
        
        print(f"{make} {model} med {hp} hästkrafter")
        

    make = input("ny bil: ")
    model = input("ny model: ")
    hp = input("ny hp: ")

    cars.append(
        {
            "make": make,
            "model": model,
            "hp": hp
        }

    

    )



"""delete = int(input("vilken vill du ta bort?"))
cars.pop(int(delete))

print(answer)"""


