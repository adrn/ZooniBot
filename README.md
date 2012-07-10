ZooniBot
========

ZooniBot is a python app designed to interact with Zooniverse users on the Planet Hunters talk site (talk.planethunters.org). 
Talk is available via the github Zooniverse/talk repository. 
The aim is to provide programmatic responses to users by searching the tags they use in their posts. 
It began life as a hackday project at the 4th dotAstronomy conference held at the Haus der Astronomie, Heidelberg, in July 2012.

Current functionality being implemented : 

#help
comment = {"body" : ‘Hiya Have you tried our [tutorial video](http://www.planethunters.org/site_guide#video "") and [site guide](http://www.planethunters.org/site_guide "") – #zoonibotans’}

if someone posts #planet or #transit if the object is an EB (eclipsing binary) -

comment ={"body": ‘You said there was a planet transit but this is a known #eclipsingbinary where there is a star moving in front of another star #zoonibotans’}

if someone posts #eclipsingbinary if the object is a planet -

comment ={"body": ‘You said this was an eclipsing binary but this is a known Kepler #planet candidate #zoonibotans’}

--------------

Zoonibot uses its Zooniverse API key to access the Talk API. It needs to identify with the username: zoonibot and the password: d1b5be9242fb65de9372
Example API calls are based on the following curl requests from @mparrish who developed the API. 

# Post a comment to a discussion
curl -H Content-Type:application/json -H Accept:application/json -X POST http://username:api_key@localhost:3000/api/comments.json -d '{
 "discussion_id": "4f65c3792fa4986c83006f06",
 "comment": {
   "body": "Some comment"
 }
}'

# Filter by tags (OR)
curl -H Content-Type:application/json -H Accept:application/json -X GET http://parrish:499cac9411b300a0a59a@localhost:3000/api/comments.json -d '{
 "tags": ["planet"]
}'

# Filter by tags with a starting timestamp
curl -H Content-Type:application/json -H Accept:application/json -X GET http://parrish:499cac9411b300a0a59a@localhost:3000/api/comments.json -d '{
 "tags": ["planet"],
 "since": "2012-01-01 00:00:00 UTC"
}'

# Return 20 results (maximum of 50 per page)
curl -H Content-Type:application/json -H Accept:application/json -X GET http://parrish:499cac9411b300a0a59a@localhost:3000/api/comments.json -d '{
 "tags": ["planet"],
 "since": "2012-01-01 00:00:00 UTC",
 "per_page": 20
}'

# Return the next 20 results
curl -H Content-Type:application/json -H Accept:application/json -X GET http://parrish:499cac9411b300a0a59a@localhost:3000/api/comments.json -d '{
 "tags": ["planet"],
 "since": "2012-01-01 00:00:00 UTC",
 "per_page": 20,
 "page": 2
}'

---------

Zoonibot also has a Twitter account (username: zoonibot, password: zoonibotHdA) and details of its functionality needs to go here. 

__________

Details of permissions for bot operation in Zooniverse projects are being worked out. For now, please ask Chris Lintott (cjl@astro.ox.ac.uk) before changing any functionality that affects what Zoonibot says in public. 
