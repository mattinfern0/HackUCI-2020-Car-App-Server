
cars_test = [
  
        {
        "make" : "Honda",
        "model" : "Civic",
        "size" : 4,
        "body_type" : "Sedan",
        "price" : 18000,
        "MPG" : 34,
        "fuel" : "gas"
        },
        {
        "make" : "Nissan",
        "model" : "Versa",
        "size"  : 6,
        "body_type" : "Sedan",
        "price" : 17000,
        "MPG" : 34,
        "fuel": "gas"
        },
        {
        "make" : "Ford",
        "model" : "Mustang",
        "size" : 2,
        "body_type" : "Coupe",
        "price" : 26670,
        "MPG" : 34,
        "fuel" : "electric"
        },
        
        {
        "make" : "BMW",
        "model" : "M3",
        "size" : 2,
        "body_type" : "Coupe",
        "price" : 26000,
        "MPG" : 34,
        "fuel" : "hybrid"
        }

    
]

cars_score = []

#key for numbers
# Commute: 1-10 : don't care - major decision maker 



user_choices_test = {
        "make": "Honda",
        "body_type" : "Coupe",
        "size": 5, # range: 1 to 10
        "price" : 30000, #max price they are comfortable with
        "commute": 6, # range: 1 to 10
        "fuel" : "electric",
        "range": 200
}


#----------------------------
#                        Match   !Match  
#   Make's weightage     : 30   : -10
#   body_type            : 10   : -3
#   price's weightage    : 40   : -20
#   size's weightage     : 20   :-5
#                       +-------
#   Total possible score : 100

 #---------------------------

def rateCars(cars, user_choices):
    print("Cars Type", type(cars))
    print("user_choices Type", type(user_choices))
    for car_dictionary in cars:
        
        score = 0
        price_diff = user_choices["price"] -car_dictionary["price"] 
        size_diff  = car_dictionary["size"] - user_choices["size"]
        #print("price_diff: ", price_diff)
        #print("size_diff: ", size_diff)
        if car_dictionary["make"] == user_choices["make"]:
            score += 500
            #print("added score of 20 for make")
        else:
            score -= 600
            #print("subbed score 10 for make")

        if car_dictionary["body_type"] == user_choices["body_type"]:
            score += 500
            #print("added 10 for body_type")
        else:
            score -= 600
            #print("subed 3 for body_type")
        if price_diff < 0:
            score -= abs(price_diff/100) *4
            #print("subbed for price_diff: ", abs(price_diff/100)*4)
            
        elif (price_diff >0 and price_diff <= 10000):
            
            score += (price_diff/100) *4
            #print(" added for price_diff  : ", (price_diff/100) *4)
        elif price_diff > 10000:
            score += (price_diff/400)
            #print("added for price_diff : ",  price_diff/100)

        score += (10 - size_diff) *2
    #   print("added for size_diff: ", (10 - size_diff) *2)
        if user_choices["fuel"] != "electric":
            print("it's gasoline")
            score += car_dictionary["MPG"] * user_choices["commute"] * 10

        if user_choices["fuel"] == car_dictionary["fuel"]:
            score += 1000
        else:
            score -= 1000

        if user_choices["fuel"] == "electric" and car_dictionary["fuel"] == "hybrid":
            score += 500

        if user_choices["fuel"] == "electric":
            try:
                score += car_dictionary["range"] *10
            except:
                pass
        cars_score.append(score)
        car_dictionary["points"] = score
        print()
        print()
        print()

    print(cars_score)
    return cars

'''
def getScoreList(carsList):
    for car_dictionary in cars:
        
        score = 0
        price_diff = user_choices["price"] -car_dictionary["price"] 
        size_diff  = car_dictionary["size"] - user_choices["size"]
        #print("price_diff: ", price_diff)
        #print("size_diff: ", size_diff)
        if car_dictionary["make"] == user_choices["make"]:
            score += 500
            #print("added score of 20 for make")
        else:
            score -= 600
            #print("subbed score 10 for make")

        if car_dictionary["body_type"] == user_choices["body_type"]:
            score += 500
            #print("added 10 for body_type")
        else:
            score -= 600
            #print("subed 3 for body_type")
        if price_diff < 0:
            score -= abs(price_diff/100) *4
            #print("subbed for price_diff: ", abs(price_diff/100)*4)
            
        elif (price_diff >0 and price_diff <= 10000):
            
            score += (price_diff/100) *4
            #print(" added for price_diff  : ", (price_diff/100) *4)
        elif price_diff > 10000:
            score += (price_diff/400)
            #print("added for price_diff : ",  price_diff/100)

        score += (10 - size_diff) *2
    #   print("added for size_diff: ", (10 - size_diff) *2)
        if user_choices["fuel"] != "electric":
            print("it's gasoline")
            score += car_dictionary["MPG"] * user_choices["commute"] * 10

        if user_choices["fuel"] == car_dictionary["fuel"]:
            score += 1000
        else:
            score -= 1000

        if user_choices["fuel"] == "electric" and car_dictionary["fuel"] == "hybrid":
            score += 500

        if user_choices["fuel"] == "electric":
            try:
                score += car_dictionary["range"] *10
            except:
                pass
        cars_score.append(score)
        print()
        print()
        print()

    print(cars_score)
'''  

        
        
        

    








