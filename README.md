# Twitter API Project

This project is a Flask web application that interacts with the Twitter API to retrieve user information and stores it in a MongoDB database.

## Features

- **User Information Retrieval:** Retrieve user information from the Twitter API based on selected fields.
- **Database Storage:** Store user information in a MongoDB database.
- **Web Interface:** Use Flask to create a web interface for interacting with the application.

# Prerequisites

## Getting Started

1. Clone the repository:

```
git clone https://github.com/CharlieCidral/twitter-api.git
cd twitter-api
```

## Twitter(X)
- Developer account.
- Create a App to integrate and config the callback link.
- Twitter API credentials (consumer key, consumer secret).

## Python^=3.8

### Packages
- pymongo
- Flask
- OAuth1Session
- json
- python-dotenv
- os

## MongoDB

- Create a database with Atlas and configure to connect with pymongo

## Docker

- Install Docker
- Build the Docker image
```
docker-compose build

```
- Run the Docker container
```
docker-compose up

```
# Usage
- Go to http://localhost:5000/ or http://127.0.0.1:5000/

![home page](https://github.com/CharlieCidral/twitter-api/assets/69029099/3ff1afd5-87ab-4371-99df-50e29017eb9d)

- Then select the info that you want return and submit.
- A message like this will appear: Please go here and authorize: 'https://api.twitter.com/oauth/authorize?oauth_token="your_auth_token"'
- After authorize, you'll be redirected to a link like this: 'http://'your_callback_link'/?oauth_token='your_auth_token'verifier='your_pin''
- The pin will be at the end of the link you were redirected to, just copy and paste it.
- Then you can go to /receive and see the return about what you submit:

![selected receive](https://github.com/CharlieCidral/twitter-api/assets/69029099/1ae72d00-7e3a-4a7f-84d0-972fcdd19096)

- You can click in Go to User Page to see the info from your database collection:

![twitter](https://github.com/CharlieCidral/twitter-api/assets/69029099/1ea8f594-e1a7-45f5-994b-bbc917b2d834)


This project was a challange made from DIO and i use the sample of code from a repository given by Twitter's documentation. 
If you want to try one, these are the free options, [User Lookup](https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/User-Lookup/get_users_me_user_context.py) and [Manage Tweets](https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Manage-Tweets/create_tweet.py).

### Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

### License
This project is licensed under the MIT License.

