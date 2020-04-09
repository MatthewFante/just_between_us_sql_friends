<h1>Just Between Us SQL Friends</h1>
<b>Rupaul's Drag Race: Analyzed</b>

This repo contains my work-in-progress final project for the Code Louisville program. 

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MatthewFante/just_between_us_sql_friends/master?filepath=just_between_us_sql_friends.ipynb)


[![nbviewer](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MatthewFante/just_between_us_sql_friends/master?filepath=just_between_us_sql_friends.ipynb)


<h3>Include a README file (or add to your project plan) the following items:</h3>
<ul>
    <li><b>What question are you answering or problem are you analyzing?</b>
        <ul>
            <li>How does a queen's performance in their main season of RuPaul's Drag Race relate to their performance in All Stars? </li>
            <li>Did the queens who won <i>actually</i> perform the best? If not, who are the <i>real</i> winningest queens of all time?</li>
        </ul>
    </li>
    <li><b>A brief overview of how you accomplished this, including any necessary background for someone to understand the problem, where your data came from, what you used from that data, any analysis you applied to the data, and what you chose to visualize/display/report in the final product</b>
        <ul>
            <li></li>
            <li></li>
        </ul>
    </li>
    <li><b>A glossary of any terms your project uses that may not be known to a reviewer - if your project topic uses specialized terminology, formulas, or other info that someone may not know, you should describe it in your README</b>
        <ul>
            <li></li>
            <li></li>
        </ul>
    </li>
    <li><b>Any special requirements, dependencies, or steps to run the project</b>
        <ul>
            <li></li>
            <li></li>
        </ul>
    </li>
</ul>




<h2 style="color:deeppink">Project Requirements</h2>

<ul>
    <li><strike>You must include a SQL database (MySQL or SQLite) where your data will be stored</strike></li>
    <li><strike>You need to include the sql or python script that creates your database</strike></li>
    <li><strike>You must include a Python script used to fetch data from a data source and load it into your SQL database</strike></li>
    <li><strike>Your data source may be an external API, database, a CSV file, JSON, or any other data source that you can read/parse via Python code</strike></li>
    <li><strike>You must include a Python script to retrieve the data from your SQL database into a Python object</strike></li>
    <li><strike>Visualize the results of your analysis using Matplotlib, Seaborn, Bokeh or another Python Data Visualization library. Your results can not be a plain text representation and you are encouraged to explore a visualization approach that clearly supports a conclusion/result of the analysis of your data.</strike></li>
    <li><strike>Your data retrieval for visualization uses at least one SQL query, meaning you can't parse records from your data set using only Python or an ORM. </strike></li>
</ul>

<h2 style="color:deeppink">Data Schema</h2>
<ul>
    <li>
        <h3 style="color:deeppink">queens_df</h3>
        <ul>
            <li>id - int</li>
            <li>name - str</li>
            <li>quote - str</li>
            <li>image_url - str</li>
            <li>miss_congeniality - bool</li>
            <li>winner - bool</li>
        </ul>
    </li>
    <li>
        <h3 style="color:deeppink">main_seasons_df</h3>  
        <ul>
            <li>season_id - int</li>
            <li>queen_id - int</li>
            <li>place - int</li>
        </ul>
    </li> 
    <li>
        <h3 style="color:deeppink">all_stars_df</h3>
        <ul>
            <li>season_id - int</li>
            <li>queen_id - int</li>
            <li>place - int</li>
        </ul>
    </li>
</ul>
