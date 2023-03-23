# Import the requests library to make HTTP requests
import requests
import pandas as pd

# Define the API endpoint for searching for users on Unsplash
endpoint = 'https://api.unsplash.com/search/users'

# Set the value for the first name to filter the results
#first_name = 'Emma'
location = 'Istanbul'

# Set up the query parameters as a dictionary with the first_name parameter
# and your Unsplash API access key as the value for the Authorization header
params = {
    #'query': first_name,
    'query': location,
    'instagram_username': 'True',
    'per_page': 100,
}
headers = {
    'Authorization': 'Client-ID <your_access_key>'
}

# Use the requests library to make an HTTP GET request to the API endpoint
response = requests.get(endpoint, params=params, headers=headers)

# Check if the request was successful by checking the status code
if response.status_code == 200:
    # If the request was successful, extract the JSON data from the response
    data = response.json()
    # Extract the 'results' key from the JSON data, which contains a list of user objects
    results = data['results']
    # Loop through the user objects and print out the 'instagram_username' and other accessible fields
    for user in results:
        if user["instagram_username"] is not None:
            print(user['instagram_username'], user['username'], user['first_name'], user['last_name'], user['total_likes'],
                 user['total_photos'], user['location'], user['twitter_username'])

else:
    # If the request was not successful, print out an error message
    print('Error: Request failed with status code', response.status_code)
