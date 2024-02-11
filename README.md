ECSE3038 LAB 2  
I had trouble with the VSCODE Github uploading hence no gitignore

Create an API that implement a POST request handler to add new people to the existing data list and a 
GET request handler that will show all added data of the person list


//////////////////////////////////////////////////////////////////
Reason for Code 
I had to do it or 0


//////////////////////////////////////////////////////////////////////
Favourite Pokemon 
Arceus 
Reason - No pokemon stronger than God.  


create_person 
This code will allow for a new entry to be made in the data list using the POST request. 
The function also checks if the data entered is valid or not. 
If the data is not valid then the request will give back an error. 
If the data is valid then it will give back success and print the entred data. 
e.g 
name": "Beef Wellington",
	"occupation": "Fry Cook",
	"address": "124 Conch Street" 

 success": true,
	"result": {
		"name": "Beef Wellington",
		"occupation": "Fry Cook",
		"address": "124 Conch Street" 
  if an invalid entry is present e.g

  	"name": "Beef Wellington",
	"occupation": "Fry Cook",
	"address": "" 

 "success": false,
"result": {
"error_message": "invalid request"

get_person 
This function allows data of every entry to be received.  

e.g 
"Beef Wellington",
"occupation": "Fry Cook",
"address": "124 Conch Street" 


