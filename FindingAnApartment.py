sd

def apt_search1(city, max_rent, min_beds, pets_allowed):
    if pets_allowed:
        print(f"""Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of {max_rent} per month...
""")
    else:
        print("""Welcome to GC Property Management! Looking up listings in Walla Walla for 1 bedroom apartments, all within a budget of $1500 per month...
""")
apt_search1("Atlanta", 4000, 5, False)

#Second apartment search
def apt_search2 (city, max_rent, min_beds= 4, pets_allowed=True):
    print(f"""Welcome to GC Property Management! Looking up listings in {city} for {min_beds} bedroom apartments that allow pets, all within a budget of {max_rent} per month...
#""")
apt_search2("Detroit",4000,)
apt_search2("Detroit", 5000, 4)
apt_search2("Atlanta", 5000, pets_allowed=True)

plus_onehundred = lambda x: x+100
print(plus_onehundred(5))
square_num = lambda x: x**2
print(square_num(2))
str_cocatenate = lambda x: f"-{x} "
print(str_cocatenate("Timeless"))
divide_by_three = lambda x: x/3
print(divide_by_three(9))