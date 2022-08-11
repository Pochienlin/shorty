# SHORTY URL Shortener

## Overview
Shorty URL includes a custom flask-based API, serverless backend and basic html/css/js front-end to create a localised shortened URL.

### Use case
1. The user inputs the desired URl into the text input box and hit 'GO'
2. Subsequently, the shortened URL appears below with a "COPY" button.
3. The webpage writes the shortened URL within the box into the clipboard
4. Once copied, the button's text changes to "COPIED!"
5. The user can paste another URL in and shorten a new URL

## Tech Stack

### Front-end
|Item|Purpose|
|----|-------|
|HTML|Mark-up contents|
|Javascript|Dynamic page functions|
|Vue.js|Lightweight JS framework for real-time feedback|
|Bootstrap|Viewport responsiveness|
|CSS|Set background color, overwriting bootstrap elements|

### Backend
|Item|Purpose|
|----|-------|
|Python|API's script language|
|Flask|Wrap python functions into API|
|Firebase|Serverless database|
|Axios|Manage API calls using cleaner code|
|Docker|Containerise API|

## Set up
### Pre-requisites - method 1
1. Docker
2. Web browser
3. Internet connection
4. WAMP/MAMP/LAMP
OR
### Pre-requisites - method 2
1. WAMP/MAMP/LAMP
2. Installed libraries under "requirements.txt"
3. Web browser
4. Internet connection

### Method 1: Using docker
1. Pull image from docker hub with `docker pull pochienlin/shorty:1.1 ./`
2. Run container using `docker run -p 5000:5000 pochienlin/shorty:1.1`
3. You should see the container running on port 5000 on localhost
4. Put the files in the repo into the root folder of your local server
    - MAMP: htdocs/shorty...
    - WAMP: www/shorty...
5. Visit the site at http://localhost/shorty

### Method 2: Running the flask app directly
1. Download all prerequisites under requirements.txt
2. Put the files in the repo into the root folder of your local server
    - MAMP: htdocs/shorty...
    - WAMP: www/shorty...
3. Go to your terminal and change directory to the repo folder > API
4. Run the app using `python shorty.py` (Win) or `python3 shorty.py` (Mac)
5. You should see the app running on port 5000 on localhost
6. Visit the site at http://localhost/shorty

## Demo
Too much to set up? Sorry for not deploying this website!
You can find a video demo [here](https://pochien.notion.site/Shorty-URL-shortener-7fb4bad552e94509b73cdb0ce00856d6)

## Other considerations
Other options for frontend include using ReactJS over VueJS. React is more popular and therefore may be easier to maintain. This project however does not require many functionalities that React has, and Vue being more lightweight allows for a less bloated stack. Vue's syntax is also relatively intuitive, so maintaining the code would not be difficult

Other options for backend include using MongoDB or MySQL based backend This will allow for more scalability and more refined queries. Firebase on the other end is more rigid, but edges out its competition because of its speed and flexibility. It allows for pay-by-use models and updates in real-time. 

For a URl shortener, users are likely to want as fast a response time as possible. Using mysql connector with flask and calling this app using HTTP methods will result in slower runtimes, especially when the data set grows. Whereas an SQL server requires further assistance to configure search algorithms or risk increasing search time with every new entry, Firebase simply returns a single response for every call. 

The data being handled here are also publically-available information, hence there is not much requirement to make the database secure. Should there be such a requirements, an API key can be used. If more access control is required, an API gateway using Kong can be included in the dockerised solution.