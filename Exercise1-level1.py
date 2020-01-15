'''
        A better solution would be to modularize the code and separate the logic for Mobiles and Shoes.15 min

Modify the code as per the below guidelines:
1.Create two functions: purchase_mobile and purchase_shoe
2.purchace_mobile() takes two parameters :price and brand
3.purchace_shoe() takes two parameeters:price and material
4.if the mobile brand is "Apple" ,discount is 10% ,else discounts 5%
5.if the shoe materisl is "leather" ,tax is 5% ,else tax is 2%
'''
def purchase_mobile(price,brand):
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price = price - price * discount / 100

    print("Total price of Mobile is "+str(total_price))

def purchase_shoe(price,material):
    if material == "leather":
        tax = 5
    else:
        tax = 2
    total_price = price + price * tax / 100

    print("Total price of Shoe is "+str(total_price))

purchase_mobile(20000,"Apple")
purchase_shoe(200,"leather")
