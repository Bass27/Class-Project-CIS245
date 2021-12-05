# import required modules
import requests

# function to request for data
def weather_data(query):
   # Enter your API key here
   api_key = "a718fa1a57ec92fb24b35bc4b2785558"
   # base_url variable to store url
   base_url = "http://api.openweathermap.org/data/2.5/weather?id=524901&appid="
   complete_url = base_url + api_key + "&" + query + "&units=imperial"
   # response object
   res=requests.get(complete_url)
   return res.json()

# function to display results
def display_results(weathers,city):
   print("{}'s temperature: {}°F ".format(city,weathers['main']['temp']))
   print("Wind speed: {} m/s".format(weathers['wind']['speed']))
   print("Description: {}".format(weathers['weather'][0]['description']))
   print("Weather: {}".format(weathers['weather'][0]['main']))
   rerunProgram()

# main function
def main():
   # Give city name
   city=input('Enter the city name or zipcode (for more precise forcast, use zipcode): ')
   print()
   # try-except block
   try:
      query='q='+city
      w_data=weather_data(query)
      display_results(w_data, city)
      print()
   except:
      print('Oops, something went wrong. Either the connection failed, invalid input, or some other unexpected error.')
      print("Please try again...")
      main()
#rerun program per user input
def rerunProgram():
   userIn = input("Would you like to search the weather for another city (y/n)? ")# input for reruning program
   if userIn.lower() == "y":# if yes
      main()# rerun program
   elif userIn.lower() == "n":# if no
      print("Thank you for using this program. See you next time.")# ending message
   else:# if anything else
      print("Invalid input, please try again...")# invalid input
      rerunProgram()# give user a chance to retry


# call main
if __name__=='__main__':
   main()
