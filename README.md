# Reddit New Notifier

This project began as an experiment to compare response times between Reddit, and primary / secondary news sources such as Reuters, AP, and the BBC, all of which push 'breaking' notifications through mobile apps.

The concept relies on parsing X news subreddit (I've been testing with /r/worldnews), and calculating an 'upvotes per minute' score for each post in the 'rising' section of the sub. If the post is gaining upvotes above a determined per minute rate, a text is send via Twilio to a configurable number.

With some tweaking of configuration options, this has shown to be anywhere between 4 to 20 minutes slower than first party news sources. This is likely due to the delay between an article being posted, which we may assume is within minutes / seconds of a breaking news story being pushed from a first party source, to users reading and crucially, voting on the article.


This project was done as a point of interest, it's wrapped inside docker if anyone wants to deploy and experiment with it themselves.

## To Deploy:

* Create a Twilio account, and provide the required API keys / target numbers inside example_config.ini.
* Rename example_config.ini -> API_Config.ini. This is configurable within ConfigLoad.py.
* On a machine running docker, run the appropriate build script for your operating system (or build it yourself). I've tested this on Windows 10 running Kinematic Alpha / Docker 17.06.2 and Ubuntu Server 16.04 LTS. 

All configuration options, including how many upvotes per minute are required to send a text, target and source numbers, as well as how to sort the parsed subreddit (rising, top, all, etc are all supported, if ineffectually.)

Enjoy!
