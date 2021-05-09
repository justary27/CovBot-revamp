# CovBot-revamp

->FrostHack 2021
#HappyXelf
By Team InCognoS


# Team Details
All of us @team_InCognoS are from IIT Roorkee. We are freshers who are interested in coding and creating new things in the process. This is our 2nd Hackathon.
Aryan Ranjan [Team Leader]
Ashish Singh
Shivam Sahu

# HappyXelf
-
Spreading smiles avoiding Covid.

## The Social Problem(s):
-Every now and then we are seeing people losing their loved ones to Covid 19 due to lack of resources sometimes just due to not having sufficient and verified leads.
-Also if you don’t have Covid you are very likely to fall into all the negativity around be it through the news, isolated environment, and so on…

## The Solution
-HappyXelf will be an attempt by us @team_InCognoS to solve the above problems. We have planned to make a website and a discord bot for this. The site will feature Covid related resources to spread awareness and also a platform where people can get verified leads or make requests for resources they might need urgently. The discord bot will do the above and also provide resources aimed specifically at reducing mental tension, isolation, and depression. We aim to donate our discord bot to Covid resource community servers.

## What will we use?
We’ll be making everything from scratch, be it the website or the Discord bot. If time permits, then we’ll also host the website and the bot on Heroku. (More may be added!)
-Website
			-Frontend
				-HTML5
				-CSS3
				-JS
			-Backend: It will be fully built using Django (v3.2.2).
		-Discord Bot: We are using the discord.py (v1.7.1) library for making the bot.
		-Database: Database for storing the required data for the bot & website (Sqlite3).
		-Libraries to be Used:
			-covid (v2.4.1) [will provide Covid Stats for countries worldwide]
			-nasapy (v0.2.7) [Nasa API]
			-newsapi-python (v0.2.6) [News API]
			-tekore (3.7.1) [Spotify API]
		-APIs to be used
			-covid19india.org [for statewise data on covid cases]
			-Zenquotes.io
			-Google Charts & Google Sheets API.
-Python (v3.9.4)

## Hacking the problem!
Coming up to going at “it”, we divided work amongst us as “Teamwork is dream work”.
I @just-ary27 handled the whole back-end & the discord bot & also worked with the APIs.
@Ashish did the whole front-end work.
@Shivam handled overlooking the database operations and also helped with the discord bot.

## What we will Solve?
We aim & intend to solve 2 problems. First, we will be trying to provide people a platform through our website where they can request for their needs like Oxygen cylinders, Medicines, Beds, plasma, etc. Also, we display the verified leads to resources from our database on our website. Secondly, we will be aiming to help people who are feeling depressed and lonely through interactive services from our discord bot. We will be donating the discord bot that we will make to a Covid resource community server where it may be used for automating the work of storing the verified leads and their retrieval also. (Yes, the bot will also store the needs and verified leads!).
## Use Cases
Our use cases target the present emergency needs & cater to any common folk whose near and dear ones may be battling against Covid-19 who has access to the internet. 
		-Providing resources on Covid-19 (from the website as well as the discord bot).
		-Helping people cope up with mental tension & depression and also spreading Covid awareness.
		-Displaying the needs & leads for better help of the diseased people.

## Future Scope
What we make here will be relevant from the very present till as long as Covid19 prevails the end of which isn’t visible anytime in the near future (even less with the news of a 3rd wave around the corner). The discord bot will also be useful for any people who are feeling depressed. Talking of future scope, we can generalize & extend the website to several diseases, also make the website more personalized for each user with better search results. It is also possible to display the needs targeted from tweets, Reddit posts, etc. We can extend our bot idea to other social media platforms like WhatsApp, Facebook, Instagram, and so on...

## How to run the project?
  -Install Everything needed from requirements.txt
  For Website:
  -``` cd CoV19 ```
  -``` python manage.py runserver 9000 ```
  For Using bot in your server:
  -https://discord.com/oauth2/authorize?client_id=835222640821796924&scope=bot
