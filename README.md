# burgers_and_beers_frontend

## Project Description
> Include:<br />
> General App Idea/Purpose<br />
Create an app where a user can rate restaurants with the best burgers and beers. 
  
> What technology stack(s) are you using for your frontend / backend?<br />
Frontend:
React
Javascript
CSS
Bootstrap
Backend:
Python
Flask
PostgreSQL

> Models including field names and their datatypes<br />
User Model:
Username= String
email= String
Password
Places Model:
Name: String
Location: String
Rating: Int
Likes: Int
Comments: String
ImageURL: Sting
Private: Boolean
> A list of routes (e.g. `POST /pins/ allows users to post a picture of a pin`)<br />
Routes:
POST /register - Register user
POST /login- Login user
GET /logout- Log out user
GET /places- Shows all places
POST /places/new - Create a new place
GET /places/:id - Show one place
PUT /places/:id - Edit one place
DELETE /places/:id - Delete one place


## Wireframes
> Wireframes with basic page layouts<br />
> Copy and paste or drag and drop your images here.
![image](https://media.git.generalassemb.ly/user/43177/files/d8ddb0d7-4c1b-49e8-8b3b-1bb190eebaf9)
![image](https://media.git.generalassemb.ly/user/43177/files/0d349817-09d6-4046-a1f2-4a69a1e65392)
![3-Register-page](https://media.git.generalassemb.ly/user/43177/files/5ea68a6e-50f2-4835-835c-206fac1dd509)
![4-Users-page](https://media.git.generalassemb.ly/user/43177/files/c25b168b-945b-4306-b1e0-d3ac44e4a5f1)
![5-Add-Place](https://media.git.generalassemb.ly/user/43177/files/bc301676-63c3-4e04-b00a-36ae83cc7bd0)
![6-Update-Place](https://media.git.generalassemb.ly/user/43177/files/8a5dac43-c259-49b2-bdbc-0997ab1315f7)
![7-Show-Place](https://media.git.generalassemb.ly/user/43177/files/c93754de-c60e-4338-be0b-3de7eb78305f)



## Feasibility Study

I plan on using Google Maps Embed API.
You can set the Maps Embed API URL as the src attribute of an iframe. When configuring a src property, the required q parameter can support a URL-escaped place name, address, plus code, or Place ID.

## User Stories
As a user, I want to see all listings of restaurants made public.
As a user, I want to be able to register or log in to my account.
As a user, I want to like a place.
As a registered user, I want to add a place.
As a registered user, I want to update a place.
As a registered user, I want to delete a  place.

### MVP Goals
Create users and places schema.
Users can log in.
Users can view all other posts.
Users can update/delete their own posts.

### Stretch Goals

Insert a static Google map of the location.
Users can insert a picture of the place.
