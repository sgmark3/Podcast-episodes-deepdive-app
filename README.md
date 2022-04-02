# Summarizing podcast episodes using topic modeling.

In the recent years podcasts have become exceedingly popular medium for content creation and dissemination.

The finished app can be found at the follwing link (https://whispering-mountain-96051.herokuapp.com/). User can choose to look at closing, opening, high, low prices
of a stock ticker for a month in the year 2021. User can also look at the change in the trading volume and percentage log return over a month of choosing. Note that the year and the months for which the data available is limited. So, use only 05-2021 to 08-2021. 

The steps and tools used to develop the app are described below.

## Step 1: Setup and deploy
- Git clone the existing template repository.
- `Procfile`, `requirements.txt`, and `setup.py` contain some default settings. If you want, you can change the email address in `setup.py` to your own, but it won't affect anything in the app.

- Create Heroku application with `heroku create <app_name>` or leave blank to
  auto-generate a name.

- Deploy to Heroku: `git push heroku master`
- You should be able to see your site at `https://<app_name>.herokuapp.com`
- A useful reference is the Heroku [quickstart guide](https://devcenter.heroku.com/articles/getting-started-with-python-o).

## Step 2: Get data from API and put it in pandas
- Use the `requests` library to grab some data from a public API. This will
  often be in JSON format, in which case `simplejson` will be useful.
- Build in some interactivity by having the user submit a form which determines which data is requested.
- Create a `pandas` dataframe with the data.

## Step 3: Plot pandas data
- Create an interactive plot from the dataframe. Some recommended libraries: Altair, Bokeh, and Plotly.
- Altair provides a simple interface for creating linked and layered plots. They can even be exported and embedded in static HTML (and remain fully interactive!) See the [documentation](https://altair-viz.github.io/)
  and be sure to check out the example gallery.
- Bokeh can be used in a wide range of applications, from simple charts to extensive dashboards with sophisticated backends. It's the most fully-featured library of these three, but you won't be using it for anything complicated in the Milestone Project. Here you can find the Bokeh [documentation](http://bokeh.pydata.org/en/latest/docs/user_guide/embed.html)
  and some [examples](https://github.com/bokeh/bokeh/tree/master/examples/embed).
- Plotly provides a range of APIs in their library. Plotly express, for instance, can be used to create commonly used plots. The Graph Objects API affords more customization, but is more complicated to use. Here is the [documentation](https://plotly.com/python/plotly-express/#gallery) for Plotly Express.
