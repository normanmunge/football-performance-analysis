# Football Player Analysis & Model Training

Football is the most followed sport in the world. According to [UEFA](https://www.uefa.com/nationalassociations/uefarankings/country/?year=2025) coefficient ratings, the top 5 leagues i.e. English (EPL, Championship etc.), Italian (Seria A), Spanish (La Liga), German (Bundesliga) and French (Ligue 1) make up the top 5 leagues with the most views. Ideally, this makes them the most competitive given the best players play in this league.

The objective of this project is to explore a sample dataset from these 5 leagues for the 2023-2024 season. This [dataset](datasets/data.csv) is sourced from [kaggle](https://www.kaggle.com/datasets/vivovinco/20222023-football-player-stats) with its original source being [Fbref](https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats). The data points collected include:

- Rk: Rank
- Player: Player’s name
- Nation: Player’s nation
- Pos: Position
- Squad: Squad’s name
- Comp: League that squad occupies
- Age: Player’s age
- Born: Year of birth
- MP: Matches played
- Starts: Matches started
- Min: Minutes played
- 90s: Minutes played divided by 90
- Goals: Goals scored or allowed
- Shots: Shots total (Does not include penalty kicks)
- SoT: Shots on target (Does not include penalty kicks)
- SoT%: Shots on target percentage (Does not include penalty kicks)
<details>
<summary>Click to view other columns!</summary>
- G/Sh: Goals per shot
- G/SoT: Goals per shot on target (Does not include penalty kicks)
- ShoDist: Average distance, in yards, from goal of all shots taken (Does not include penalty kicks)
- ShoFK: Shots from free kicks
- ShoPK: Penalty kicks made
- PKatt: Penalty kicks attempted
- PasTotCmp: Passes completed
- PasTotAtt: Passes attempted
- PasTotCmp%: Pass completion percentage
- PasTotDist: Total distance, in yards, that completed passes have traveled in any direction
- PasTotPrgDist: Total distance, in yards, that completed passes have traveled towards the opponent’s goal
- PasShoCmp: Passes completed (Passes between 5 and 15 yards)
- PasShoAtt: Passes attempted (Passes between 5 and 15 yards)
- PasShoCmp%: Pass completion percentage (Passes between 5 and 15 yards)
- PasMedCmp: Passes completed (Passes between 15 and 30 yards)
- PasMedAtt: Passes attempted (Passes between 15 and 30 yards)
- PasMedCmp%: Pass completion percentage (Passes between 15 and 30 yards)
- PasLonCmp: Passes completed (Passes longer than 30 yards)
- PasLonAtt: Passes attempted (Passes longer than 30 yards)
- PasLonCmp%: Pass completion percentage (Passes longer than 30 yards)
- Assists: Assists
- PasAss: Passes that directly lead to a shot (assisted shots)
- Pas3rd: Completed passes that enter the 1/3 of the pitch closest to the goal
- PPA: Completed passes into the 18-yard box
- CrsPA: Completed crosses into the 18-yard box
- PasProg: Completed passes that move the ball towards the opponent’s goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area
- PasAtt: Passes attempted
- PasLive: Live-ball passes
- PasDead: Dead-ball passes
- PasFK: Passes attempted from free kicks
- TB: Completed pass sent between back defenders into open space
- PasPress: Passes made while under pressure from opponent
- Sw: Passes that travel more than 40 yards of the width of the pitch
- PasCrs: Crosses
- CK: Corner kicks
- CkIn: Inswinging corner kicks
- CkOut: Outswinging corner kicks
- CkStr: Straight corner kicks
- PasGround: Ground passes
- PasLow: Passes that leave the ground, but stay below shoulder-level
- PasHigh: Passes that are above shoulder-level at the peak height
- PaswLeft: Passes attempted using left foot
- PaswRight: Passes attempted using right foot
- PaswHead: Passes attempted using head
- TI: Throw-Ins taken
- PaswOther: Passes attempted using body parts other than the player’s head or feet
- PasCmp: Passes completed
- PasOff: Offsides
- PasOut: Out of bounds
- PasInt: Intercepted
- PasBlocks: Blocked by the opponent who was standing in the path
- SCA: Shot-creating actions
- ScaPassLive: Completed live-ball passes that lead to a shot attempt
- ScaPassDead: Completed dead-ball passes that lead to a shot attempt
- ScaDrib: Successful dribbles that lead to a shot attempt
- ScaSh: Shots that lead to another shot attempt
- ScaFld: Fouls drawn that lead to a shot attempt
- ScaDef: Defensive actions that lead to a shot attempt
- GCA: Goal-creating actions
- GcaPassLive: Completed live-ball passes that lead to a goal
- GcaPassDead: Completed dead-ball passes that lead to a goal
- GcaDrib: Successful dribbles that lead to a goal
- GcaSh: Shots that lead to another goal-scoring shot
- GcaFld: Fouls drawn that lead to a goal
- GcaDef: Defensive actions that lead to a goal
- Tkl: Number of players tackled
- TklWon: Tackles in which the tackler’s team won possession of the ball
- TklDef3rd: Tackles in defensive 1/3
- TklMid3rd: Tackles in middle 1/3
- TklAtt3rd: Tackles in attacking 1/3
- TklDri: Number of dribblers tackled
- TklDriAtt: Number of times dribbled past plus number of tackles
- TklDri%: Percentage of dribblers tackled
- TklDriPast: Number of times dribbled past by an opposing player
- Press: Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball
- PresSucc: Number of times the squad gained possession within five seconds of applying pressure
- Press%: Percentage of time the squad gained possession within five seconds of applying pressure
- PresDef3rd: Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the defensive 1/3
- PresMid3rd: Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the middle 1/3
- PresAtt3rd: Number of times applying pressure to opposing player who is receiving, carrying or releasing the ball, in the attacking 1/3
- Blocks: Number of times blocking the ball by standing in its path
- BlkSh: Number of times blocking a shot by standing in its path
- BlkShSv: Number of times blocking a shot that was on target, by standing in its path
- BlkPass: Number of times blocking a pass by standing in its path
- Int: Interceptions
- Tkl+Int: Number of players tackled plus number of interceptions
- Clr: Clearances
- Err: Mistakes leading to an opponent’s shot
- Touches: Number of times a player touched the ball
- TouDefPen: Touches in defensive penalty area
- TouDef3rd: Touches in defensive 1/3
- TouMid3rd: Touches in middle 1/3
- TouAtt3rd: Touches in attacking 1/3
- TouAttPen: Touches in attacking penalty area
- TouLive: Live-ball touches
- DriSucc: Dribbles completed successfully
- DriAtt: Dribbles attempted
- DriSucc%: Percentage of dribbles completed successfully
- DriPast: Number of players dribbled past
- DriMegs: Number of times a player dribbled the ball through an opposing player’s legs
- Carries: Number of times the player controlled the ball with their feet
- CarTotDist: Total distance, in yards, a player moved the ball while controlling it with their feet, in any direction
- CarPrgDist: Total distance, in yards, a player moved the ball while controlling it with their feet towards the opponent’s goal
- CarProg: Carries that move the ball towards the opponent’s goal at least 5 yards, or any carry into the penalty area
- Car3rd: Carries that enter the 1/3 of the pitch closest to the goal
- CPA: Carries into the 18-yard box
- CarMis: Number of times a player failed when attempting to gain control of a ball
- CarDis: Number of times a player loses control of the ball after being tackled by an opposing player
- RecTarg: Number of times a player was the target of an attempted pass
- Rec: Number of times a player successfully received a pass
- Rec%: Percentage of time a player successfully received a pass
- RecProg: Completed passes that move the ball towards the opponent’s goal at least 10 yards from its furthest point in the last six passes, or any completed pass into the penalty area
- CrdY: Yellow cards
- CrdR: Red cards
- 2CrdY: Second yellow card
- Fls: Fouls committed
- Fld: Fouls drawn
- Off: Offsides
- Crs: Crosses
- TklW: Tackles in which the tackler’s team won possession of the ball
- PKwon: Penalty kicks won
- PKcon: Penalty kicks conceded
- OG: Own goals
- Recov: Number of loose balls recovered
- AerWon: Aerials won
- AerLost: Aerials lost
- AerWon%: Percentage of aerials won
</details>
<br>
The challenge is sourced from [kaggle](https://www.kaggle.com/datasets/tevintemu/tanzania-tourism-classification-challenge) in case you want to find out more, visit the link.

This project is for anyone interested in data science especially tailored towards beginners. It's also interesting for football enthusiasts, commentators and data scientists venturing into sports analytics. Even though the data is from tracking the live records of the leagues, the data used is purely for education purposes and caution must be taken for anyone interested in using it for commercial purposes.

## 1. Objectives, Planning and Folder Structure

### 1.1. Objectives

The [notebook](/football-performance-eda.ipynb) does an exploratory data analysis and model training on the data using a pandas DataFrame. The steps include:

1. Load the dataset from csv
2. Data Wrangling
   - Understanding the data - statistical summary, generating a ydata_profile
   - Cleaning of the data - handling missing values, wrong values, duplicate values
3. Analysis of the following questions:
   - Which team has collectively scored the most goals in the Premier League?
   - Who scored the most goals across the leagues?
   - Which leagues score/concede the most goals?
   - What is the average number of minutes played in the season for all players?
   - What is the correlation between age and minutes played by players?
4. Visualization of the answered questions above
5. Training model to forecast the minutes player taking age as a consideration

### 1.2. Folder Structure

The repository contains:

1. [Datasets Directory](/datasets/) - This directory holds our dataset - [/datasets/data.csv](/datasets/data.csv, 'football player stats')

2. [Requirements.txt] (/requirements.txt) - Showing the necessary libraries and dependencies to run the notebook.
3. Files
   - [football-performance-eda notebook](football-performance-eda.ipynb) - A notebook to conduct our analysis and run our model experiments
   - [main.py](main.py) - A python script to run our model in production based out of our notebook
   - [model_performance.csv] - CSV to store our model performance to track how it's improved over time
4. [Gitignore File](/.gitignore) - File to ignore files and directories from being pushed to the remote repository
5. [README.md File](/README.md) - Guiding instructions for describing and running the project.

## 2. Setting up your local environment

This section guides you on how to setup your environment and run the repository on your local environment.

### 2.1. Creating a virtual environment

Create a virtual environment to install and manage the libraries to isolate them from your global environments.

To create a virtual environment, run the command below on your terminal:

```bash
python -m venv 'myenv_name'
```

Disclaimer: This approach is recommended for Linux and Mac environments. There might be a different approach for setting up in Windows environments.

### 2.2. Activating your environment

To activate your environment on linux or mac operating system. Run the command below on your terminal.

```bash
source /path/to/myenv_name/bin/activate
```

To activate your environment on a windows environment:

```bash
source \path\to\myenv_name\Scripts\activate
```

### 2.3. Deactivating your environment

Once you're done working on the repository, <b><i>REMEMBER</i></b> to deactivate your virtual environment in order to separate your local project dependencies.

To deactivate your environment on a linux or mac operating system. Run the command below on your terminal:

```bash
deactivate
```

## 3. Libraries and Installations

### 3.1. Required Libraries

The important libraries used in this environment are:

1. Pandas - Used for manipulation, exploration, cleaning and analyzing of your dataset.
2. Numpy - Used for mathematical and statistical purposes often to prepare your dataset for machine learning
3. Matplotlib - Used for visualization purposes to highlight discovered patterns in your dataset to stakeholders in form of graphs
4. Seaborn - Used for visualization purposes to highlight discovered patterns in your dataset to stakeholders in form of graphs
5. Matplotlib - Used for visualization purposes to highlight discovered patterns in your dataset to stakeholders in form of graphs
6. Scklearn - Training and evaluating our models
7. Chardet - Checking file encodings
8. Jupyter lab - Used to run and experiment on your notebook in your local environment

The above listed libraries are the core ones used in the repository. However, during installation you'll notice other dependencies installed that enable to work as expected. They are highlighted on the [requirement.txt](/requirements.txt) file.

### 3.2. Installation of the Libraries

Ensure you are have a version python > 3 installed and running on your local environment in order to to be able to install the libraries and run the notebook. Afterwards, ensure the virtual environment you created above is active before running the installation commands below on your terminal.

To install the libraries run:

```bash
pip install pandas numpy matplotlib seaborn jupterlab chardet scikit-learn
```

You can also install all the libraries by running:

```bash
pip install requirements.txt
```

## 4. Starting your notebook

To run your notebook in your local environment, we'll require the jupyter lab library installed. Afterwards, run the command below on your terminal:

```bash
jupyter lab *optional_file_name*
```
