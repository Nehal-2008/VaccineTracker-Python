from cowin_api import CoWinAPI

district_id = '188'  # Random Id
date = '14-05-2021'  # Optional. Takes today's date by default
min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit

cowin = CoWinAPI()
available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
print(available_centers)

#188 district id state id = 12

# TO TAKE OUT YOUR STATE ID DO THIS 
'''cowin = CoWinAPI()
   states = cowin.get_states()
   print(states)'''

# TO TAKE OUT YOUR DISTRICT ID DO THIS
'''
   state_id = '21' # random id
   cowin = CoWinAPI()
   districts = cowin.get_districts(state_id)
   print(districts)'''

# TO FIND SLOT ACCORDING TO YOUR PINCODE
'''pin_code = "400080"
   date = '03-05-2021'  # Optional. Default value is today's date
   min_age_limit = 18  # Optional. By default returns centers without filtering by min_age_limit
   
   cowin = CoWinAPI()
   available_centers = cowin.get_availability_by_pincode(pin_code, date, min_age_limit)
   print(available_centers)'''