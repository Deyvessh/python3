
state_in_india = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                  "Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra",
                  "Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana",
                  "Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh",
                  "Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]


print(state_in_india) # it will printout all the states and UTs in the list
print("\n")

num_of_states = len(state_in_india)

# index out of error

# Here, below - why (list index out of range) becasue len function counted the number of content in the list so, 36
# but the index is 36 - 1 = 35 cause index starts from 0


# print(state_in_india[num_of_states])

# print(state_in_india[36])
                          
print(state_in_india[35]) # printed the last content in list which is 'Puducherry'

