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


    position = int(input("vilken vill du ändra?"))
    cars.pop(int(position))

    new_make = input("vilken är den nya märke: ")
    new_model = input("vilken är den modellen: ")
    new_hp = input("vilken är den nya hästkraften: ")
    cars[position]["make"] = new_make
    cars[position]["model"] = new_model
    cars[position]["hp"] = new_hp
    print(f"{make} {model} med {hp}")
