import pandas as pd

food_list = pd.read_excel('Food List.xlsx')

stall_name = [i for i in food_list["stall_name"]]
item_name = [i for i in food_list["item_name"]]
price = [i for i in food_list["price"]]
delivery = [i for i in food_list["delivery_service"]]

# Iterating through food_list to create responses similar to the length of the list
# print(food_list)

responses = []

for i in range(len(food_list)):
    responses.append("{food} is sold by {stall} stall. The price is RM {price}. Delivery status - {deli}."
                     .format(food=item_name[i],stall=stall_name[i],price=price[i],deli=delivery[i]))

# print(len(responses))

response_time = "Dear customer, our latest operation time is from 10am to 7pm everyday."
responses.append(response_time)

blank_spot = "food"

