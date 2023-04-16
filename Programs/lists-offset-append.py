
state_in_india = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana",
                  "Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra",
                  "Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana",
                  "Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh",
                  "Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

print(state_in_india) # it will carry out every state we put in the list
print("\n")

print(state_in_india[3]) # indexing - Bihar would be the output

state_in_india.append("Khalistan")

print(state_in_india) # khalistan is added at the end of the list as we appended it (append will only add the item at last)
print("\n")

state_in_india.extend(["Konkan", "Kosal", "Awadh"]) # i have added a list of items in the exisiting list and these are added at last

print(state_in_india)
print("\n")

state_in_india[20] = "Chota Punjab" # we can change the anything in list by knowing their index
print(state_in_india)