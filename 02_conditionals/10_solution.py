animal = input("Enter the animal: \n Dog \n Cat \n ")
age = int(input("Enter the age: "))

if(animal == "Dog" and age < 2):
    print("Puppy Food")
elif(animal == "cat" and age >5):
    print("Senior Cat Food")