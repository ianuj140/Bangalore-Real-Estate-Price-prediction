import json
import pickle
import numpy as np

__data_columns=None
__locations=None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
     #the numpy list.index() method will throw an error if the index of a location is not found, so I use a try catch block.
   load_saved_artefacts()
   try:
    loc_index = __data_columns.index(location.lower())   #the input location is converted to lower case because in the columns.json file all locations are given in lower case.
   except:
       loc_index=-1

   x = np.zeros(244)
   x[0] = sqft
   x[1] = bath
   x[2] = bhk
   if loc_index >= 0:
        x[loc_index] = 1

   return  round(__model.predict([x])[0], 2)


def get_location_names():
     load_saved_artefacts()
     return __locations

def load_saved_artefacts():     #this will load the pickle file and the columns file.
    global __data_columns    # these two variables should be read as global variables
    global __locations


    with open("C:/Code/BangaloreHousePrices1/server/artefacts/columns.json",'r') as f:
      __data_columns=json.load(f)['data_columns']
      __locations=__data_columns[3:]

#now we can load pickle model into __model

    global __model

    with open("C:/Code/BangaloreHousePrices1/server/artefacts/banglore_home_prices_model.pickle","rb") as f:
        __model= pickle.load(f)


if  __name__=='__main__' :

    print(get_estimated_price('6th phase jp nagar',2000,3,2))
    print(get_estimated_price('Rajaji Nagar',1000,3,2))
    print(get_estimated_price('Ejipura',1000,3,2))  #falls under "other" locations
    print(get_estimated_price('1st block jayanagar',1000,3,2))  #falls under "other" locations

