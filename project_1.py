user = {"bob" : "123", "ann" : "pass", "mike": "password123", "liz": "pass123"}
input_username = input("Uzivateli zadej sve uzivatelske jmeno:")
input_password = input("Uzivateli zadaj sve heslo:")


znak = "-"
jmeno = "Tomas Kristofik"
email = "kristofikt@gmail.com"
discord = "tomask_96697"
projekt = "projekt_1.py: první projekt do Engeto Online Python Akademie"

print(znak * 30)
print("\n")

print(projekt)
print(jmeno)
print(email)
print(discord)
print("\n")

print(znak * 30)

# Compare the inputs with the dictionary
if input_username in user and user[input_username] == input_password:
    print("username:",input_username)
else:
    print("unregistered user, terminating the program..")







                                        