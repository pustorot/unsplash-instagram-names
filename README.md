# unsplash-instagram-names
A simple query that can get instagram names of unsplash users

In this code, we first import the requests library, which provides a simple interface for making HTTP requests. We then define the API endpoint for searching for users on Unsplash and set the value for the first_name variable to filter the results.

Next, we set up the query parameters as a dictionary with the first_name parameter (as a filtering sample), and set the Authorization header to include your Unsplash API access key. We then use the requests library to make an HTTP GET request to the API endpoint, passing in the query parameters and headers as arguments.

We check if the request was successful by checking the status code of the response. If it was successful, we extract the JSON data from the response and extract the results key, which contains a list of user objects. We then loop through the user objects and print out the instagram_username and username fields for each one.

If the request was not successful, we print out an error message.
