# Predict-NBA-player-Points_End-to-end-Project :man_scientist: :hugs: :computer:

![screem.png](https://github.com/M-MSilva/Predict-NBA-player-Points_End-to-end-Project/blob/master/Images/NBA_end_to_end_project/allPictures.png) 

## Important notes about the project

This project was built with numerous tools and technologies, this is a summary document. Therefore, if you want to obtain more statistical and computational information see [Google Colaboratory](https://github.com/M-MSilva/Predict-NBA-player-Points_End-to-end-Project/blob/master/Jupyter_Notebook_Projects/Predict_NBA_player_Points.ipynb), to read about the conclusions found about the project, analyze the [Report](https://github.com/M-MSilva/Predict-The-Status-of-Loan-End-to-End-Project/blob/master/Report/Loan_Project_M_MSilva.pdf). You can also access application created in [Web App](https://predict-nba-player-points-mm.herokuapp.com/) and see how I collected the data with [Web Scraping](https://github.com/M-MSilva/Predict-NBA-player-Points_End-to-end-Project/blob/master/Jupyter_Notebook_Projects/Web_Scraping_NBA.ipynb) :roll_eyes:.

## About this project

The objective of this project is to predict the points of a basketball player, in addition we **answer some businesses questions** that are grounded on the jupyter notebook. Also, this is a complete project as we go through several steps of a usual data science project such as **web scraping** (data collection), feature engineering, data cleansing, data transformation, data visualization, data analysis, data, modeling and **cloud deployment**.

## Applications 

The current project can be used to help an athlete in his training to know how many points he would make based on some information, and it can also be used in competitions and betting. Although this program is part of my personal portfolio, feel free to use it for studies, repairs and improvements. :call_me_hand:

## Motivation
This project was developed to be part of my personal portfolio and served both to test my skills and for my learning, since countless technologies could be used in it. Despite being an end-to-end project, it still needs some future improvements, such as having a larger and more diverse dataset. :smiley:

## Functionalities

### Developed Web APPs:

* Enter athlete data and the like;
* Find out how many points an athlete would have.

### Web APP included by Streamlit

* Rerun;
* Automatically update the app when the underlying code is updated;
* Enable wide mode so the app takes up the entire width of the screen;
* Choose by dark or light theme;
* Record a video or audio of the screen;
* Report a bug;
* Get Help;
* About.


## Instructions to run and/or compile the code

### Initial Requirements

The application is already running and it is not necessary to install anything on your machine, however, if you want to run the application locally, you must install the  [Python](https://www.python.org/downloads/release/python-390/) language on your machine. In addition, you must have the libraries listed below on your machine.

### Built With

* [Pandas 1.4.1](https://pypi.org/project/pandas/);
* [Imblearn 0.0](https://pypi.org/project/imblearn/);
* [pickle-mixin 1.0.2](https://pypi.org/project/pickle-mixin/);
* [numpy 1.22.2](https://pypi.org/project/numpy/);
* [Streamlit 1.6.0](https://pypi.org/project/streamlit/);
* [scikit-learn 1.0.2](https://pypi.org/project/scikit-learn/);
* [xgboost 0.90](https://pypi.org/project/xgboost/0.90/);
* [Requests 2.27.1](https://pypi.org/project/requests/);
* [Beautifulsoup 4.10.0](https://pypi.org/project/beautifulsoup4/).

Hosted In:

* heroku


### Running the Code

The installations of the libraries are already explained in the links above, but if you want to be in the same versions I do:

```bash
pip install scikit-learn==1.0.2
```
```bash
pip install streamlit==1.6.0
```
```bash
pip install numpy==1.22.2
```
```bash
pip install pickle-mixin==1.0.2
```
```bash
pip install pandas==1.4.1
```
```bash
pip install imblearn==0.0
```

```bash
pip install xgboost==0.90
```

done, go to the Deploy folder and type:

```bash
streamlit run PredictPointsWebAPP.py
```


and see the application run on your machine. :open_mouth:


## Contributing

Criticism, doubts and suggestions feel free to send me:

e-mail: marcosmatheusdepaivasilva@gmail.com

LinkedIn: linkedin.com/in/marcos-silva-089699b3 :hugs:

## Author

Marcos Matheus de Paiva Silva

## Credits

Web scraping was done from https://www.nbastuffer.com/player-stats/. The code written in Google Colaboratory was based on the steps of the book Aurelien Geron - hands on machine learning-2019. In addition, this code was developed based on everything I learned from: Jesse E.Agbe, Siddhardhan, Lucas Grassano Lattari, Shashank Kalanithi, Walisson Silva, Israel Dryer, Fernando Nakamuta,  Alex Freberg.


## License

This project is licensed under the MIT License - see the file [LICENSE](LICENSE) for more details.
