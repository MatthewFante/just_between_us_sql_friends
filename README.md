
<h1>Just Between Us SQL Friends</h1>
<b>Rupaul's Drag Race: Analyzed</b>

<img src="media/logo.png" />

<p>This repo contains my final project for the Code Louisville program. A practical of exploration Python for data science, including: Pandas data structures, SQL Database manipulation, and data visualization using MatPlotLib and Bokeh.</p>

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/MatthewFante/just_between_us_sql_friends/master?filepath=just_between_us_sql_friends.ipynb)

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
            <li>The data in this project is provided courtesy of NoKeyNoShade.party, the Internet's Premier Competitive Female Impersonation Data API.</li>
            <li>Data manpulation is done using the pandas and sqlite3 libraries.</li>
            <li>Data visualization is done using the matplotlit and bokeh libraries.</li>
        </ul>
    </li>
    <li><b>A glossary of any terms your project uses that may not be known to a reviewer - if your project topic uses specialized terminology, formulas, or other info that someone may not know, you should describe it in your README</b>
        <ul>
            <li>No special terminology is needed to understand the development side of things.</li>
            <li>For the uninitiated, a glossary of Drag Queen lingo can be found <a href="https://rupaulsdragrace.fandom.com/wiki/RuPaul%27s_Drag_Race_Dictionary">here</a>.</li>
        </ul>
    </li>
    <li><b>Any special requirements, dependencies, or steps to run the project</b>
        <ul>
            <li>This project can be viewed in your favorite Jupyter Notebook environment (I used JupyterLab).</li>
            <li>The following libraries are required:
                <ul>
                    <li>pandas</li>
                    <li>matplotlib</li>
                    <li>bokeh</li>
                </ul>
            </li>
            <li>In most cases, the required libraries can be installed from inside the project. 
            <li>I've included some additional non-project specific functions in <i>helper.py</i> to make checking and installing dependencies a little easier.</li>
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
