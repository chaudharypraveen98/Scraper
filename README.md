# Scraper
A scraper script which is running on python's framework Flask and Fast Api can scrape BoxOfficeMojo website. We are using the Ngrok to deploy our localhost to web.


### What we are going to build?
1. We are creating a script to scrape the BoxOfficeMojo and export it to excel using the [pandas library](https://pandas.pydata.org/) by making Dataframe using the nested dictionary.

2. Then, setting up the [Flask](https://flask.palletsprojects.com/en/2.0.x/) Server to run periodic scraping using the get request on a particular url endpoint after a certain interval of time.

3. Then, making a url endpoint to serve the data which we had scraped till now.

4. We are making our localhost server accessible from anywhere using the [Ngrok](https://ngrok.com/).

5. Lastly, We are making a cmdlet or powershell script to run from anywhere wether command prompt or window power shell.