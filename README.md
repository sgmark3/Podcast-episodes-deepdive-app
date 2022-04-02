# Summarizing podcast episodes using topic modeling.

In the recent years podcasts have become an exceedingly popular medium for content creation and dissemination. Not only there more listeners but also more content creators. Due to the availability of a huge variety of podcasts, it is evident that a more sophisticated framework is needed to categorize the podcast episodes than a genre-based classification scheme. To that end, topic modelling is a viable candidate methodology for finding the key topics that describe a collection of podcast episodes (equivalent to a corpus of documents). The following streamlit application is a platform where a user (any podcast enthusiast) can choose 1. a genre from the given collection, 2. average duration of the episode, and 3. a set of keywords that they're looking for as describing an episode (words seperated by commas). Based on this information, the models suggest a maximum of three episodes. The output consists of the podcast name, episode name, episode duration, description of the episodes and the url of the podcast episodes (if available).    


The steps and tools used to develop the app are described below.

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `Procfile`, `requirements.txt`, and `setup.py` contain some default settings. If you want, you can change the email address in `setup.py` to your own, but it won't affect anything in the app.

- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.

- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).
