import json
import urllib
import requests
import psycopg2
import os.path
import sys

from os import path
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, 
                             QWidget,
                             QHBoxLayout,
                             QVBoxLayout,
                             QGridLayout,
                             QMainWindow,
                             QPushButton,
                             QLineEdit,
                             QListWidget,
                             QLabel,
                             QSizePolicy,
                             QScrollArea,
                             QSpacerItem,
                             QComboBox)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = QWidget()
        self.country = ''
        self.widget.setStyleSheet("color:white; background-color: black;")
        self.setCentralWidget(self.widget)
        self.setWindowTitle("World Weather")
        self.setFixedSize(500, 100)
        self.mainLayout = QVBoxLayout()
        self._horizontal_layout = QHBoxLayout()
        self.mainLayout.addLayout(self._horizontal_layout)
        self.widget.setLayout(self.mainLayout)
        self.display = QLineEdit(self)
        self.OkButton = QPushButton('OK', self)
        self.OkButton.setStyleSheet("color:black; background-color: white;")
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('COUNTRY: ')
        self.OkButton.resize(50, 32)
        self.display.resize(250, 30)
        self._horizontal_layout.addWidget(self.nameLabel)
        self._horizontal_layout.addWidget(self.display)
        self._horizontal_layout.addWidget(self.OkButton)
        self.OkButton.clicked.connect(self._clickMethod_single_country)

    def _clickMethod_single_country(self):
        try:
            
        self.country = self.display.text()
        # self.setFixedSize(500, 500)
        self.all_label = QLabel(self)
        main_body_function(self.country)
        connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres', password='1111')
        inserting_weather_to_capital(connection, self.country)
        cursor = connection.cursor()
        cursor.execute(f"select cities.capitalname, cities.weather_description, cities.temperature from cities left join countries on cities.capitalname = countries.capitalname")
        correct = cursor.fetchall()
        print(correct)
        connection.commit()
        cursor.close()
        self.all_label.setText(f"""Country: {self.country}, capital: {correct[0][0]}, weather: {correct[0][1]}, temperature: {correct[0][2]}""")
        self.mainLayout.addWidget(self.all_label)
        self.all_label.show()
        print(correct)
    
    def _clickMethod_all_countries(self):
        pass
           

def create_countries_table(connection):
    if path.exists("capitals.json"):
        json_file = open("capitals.json")
        data = json.load(json_file)
    else:
        source = urllib.request.urlopen("http://techslides.com/demos/country-capitals.json") 
        data = json.loads(source.read())
        with open('capitals.json','w') as f:
            json.dump(data, f, indent=4)

    cursor = connection.cursor()
    try: 
        cursor.execute('CREATE TABLE capitals(id serial primary key, countryname varchar(40), capitalname varchar(40))')
        print("countries created")
        connection.commit()
        for item in data:
            cursor.execute(f"INSERT INTO capitals(countryname, capitalname) VALUES(%s, %s)", (item['CountryName'], item['CapitalName']))
            connection.commit()
        print("countries added")
        cursor.close()
    except:
        print('database is created already')
        cursor.close()
        connection.rollback()

def create_list_of_capitals(connection):
    cursor1 = connection.cursor()
    try:
        cursor1.execute('CREATE TABLE cities (id serial primary key, capitalname varchar(40), weather_description varchar(40), temperature integer)')
        cursor1.close()
        connection.commit()
        print("capitals created")
    except:
        print('database is created already')
        connection.rollback()

def inserting_weather_to_capitals_all(connection):
    cursor = connection.cursor()
    cursor.execute('select capitalname from countries')
    cities = cursor.fetchall()
    print(f"cities: {cities}")
    for item in cities:
        if item != 'N/A':
            try:
                database_weather = requests.get('http://api.openweathermap.org/data/2.5/weather?',
                                                {'q': item, 
                                                'units': 'metric',
                                                'appid':'a5c5f26e7e133daa411606be2347d43c',
                                                'lang':'ua'})
                database_weather = database_weather.json()
                cursor.execute(f"insert into cities (capitalname, weather_description, temperature) values (%s, %s, %s)", (item, database_weather['weather'][0]['description'], database_weather['main']['temp']))
                connection.commit()
            except Exception:
                pass
    cursor.close()

def inserting_weather_to_capital(connection, country):
    cursor = connection.cursor()
    cursor.execute(f"select countries.capitalname from countries where countries.countryname = '{country}'")
    cities = cursor.fetchall()
    print(f"cities: {cities}")
    item = cities[0][0]
    print(item)
    try:
        database_weather = requests.get('http://api.openweathermap.org/data/2.5/weather?',
                                        {'q': item, 
                                        'units': 'metric',
                                        'appid':'a5c5f26e7e133daa411606be2347d43c',
                                        'lang':'ua'})
        database_weather = database_weather.json()
        cursor.execute(f"insert into cities (capitalname, weather_description, temperature) values (%s, %s, %s)", (item, database_weather['weather'][0]['description'], database_weather['main']['temp']))
        connection.commit()
    except Exception:
        pass
    cursor.close()

def main_body_function(city):
    connection = psycopg2.connect(host='localhost', database='postgres', port=5432, user='postgres', password='1111')
    print('Connection established')
    try:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE cities')
        print("cities dropped")
        cursor.close()
        connection.commit()
    except Exception:
        pass
    create_countries_table(connection)
    create_list_of_capitals(connection)
    
    connection.close()

def main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main_window()        