import requests
import json
import sys

from datetime import date
from datetime import datetime
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
                             QComboBox)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.number_of_days = 1
        self.option = 0
        self.setWindowTitle("Weather App")
        self.setFixedSize(500, 100)
        self.mainLayout = QVBoxLayout()
        self._horizontal_layout = QHBoxLayout()
        self.mainLayout.addLayout(self._horizontal_layout)
        self.widget.setLayout(self.mainLayout)
        self.resource = ''
        self.display = QLineEdit(self)
        self.OkButton = QPushButton('OK', self)
        self.nameLabel = QLabel(self)
        self.nameLabel.setText('CITY: ')
        self.combo = QComboBox(self)
        self.combo.addItems(["Today","5 Days"])
        self.combo.resize(250,32)
        self.OkButton.resize(50, 32)
        self.display.resize(250, 30)
        self._horizontal_layout.addWidget(self.nameLabel)
        self._horizontal_layout.addWidget(self.display)
        self._horizontal_layout.addWidget(self.OkButton)
        self.mainLayout.addWidget(self.combo)

        self.display.setStyleSheet("color: blue;"
                        "background-color: yellow;"
                        "selection-color: yellow;"
                        "selection-background-color: blue;")
        self.OkButton.clicked.connect(self._clickMethod)
        self.combo.activated[str].connect(self.options) 
    
    def options(self, value):
        if value == '5 Days':
            self.number_of_days = 5
        else:
            self.number_of_days = 1

    def _add_QLabels(self):
        self.weather = QLabel()
        self.weather_main = QLabel()
        self.weather_wind = QLabel()
        self.weather_sun = QLabel()
        self.weather.setAlignment(Qt.AlignCenter)
        self.weather_main.setAlignment(Qt.AlignCenter)
        self.weather_wind.setAlignment(Qt.AlignCenter)
        self.weather_sun.setAlignment(Qt.AlignCenter)
        self.mainLayout.addWidget(self.weather)
        self.mainLayout.addWidget(self.weather_main)
        self.mainLayout.addWidget(self.weather_wind)
        self.mainLayout.addWidget(self.weather_sun)
        pass

    def _remove_QLabels(self):
        self.weather.clear()
        self.weather_main.hide()
        self.weather_wind.hide()
        self.weather_sun.hide()

    def _clickMethod(self):
        if self.option == 0:
            self._add_QLabels()
            self.option += 1
        elif self.option != 0:
            self._remove_QLabels()
            self.option = 0

        if self.number_of_days == 1:
            self.setFixedSize(500, 500)
            city = self.display.text()
            try:
                resource = requests.get('http://api.openweathermap.org/data/2.5/weather?', {'q':city, 'units': 'metric', 'appid':'a5c5f26e7e133daa411606be2347d43c', 'lang':'ua'})
                resource = resource.json()
                self.show_weather_1(resource)
            except Exception:
                return
        else:    
            self.setFixedSize(500, 250)
            city = self.display.text()
            try:
                resource = requests.get('http://api.openweathermap.org/data/2.5/forecast?', {'q':city, 'units': 'metric', 'appid':'a5c5f26e7e133daa411606be2347d43c', 'lang':'ua'})
                resource = resource.json()
                self.show_weather_5(resource)
            except Exception:
                return
            
    def show_weather_1(self, resource):
        for item in resource.json().keys():
                if item == 'weather':
                    self.weather.setText(f"""
WEATHER

condition: {resource.json()[item][0]['main']}
description: {resource.json()[item][0]['description']}""") 
                
                if item == 'main':
                    self.weather_main.setText(f"""
TEMPERATURE

Temperature: {resource.json()[item]['temp']}
Feels like: {resource.json()[item]['feels_like']}
Min temperature: {resource.json()[item]['temp_min']}
Max temperature: {resource.json()[item]['temp_max']}
Pressure: {resource.json()[item]['pressure']}
Humidity: {resource.json()[item]['humidity']}""")
                
                if item == 'wind':
                    self.weather_wind.setText(f"""
WIND

Speed: {resource.json()[item]['speed']} meter/sec")
Direction: {resource.json()[item]['deg']}°""")
                
                if item == 'sys':
                    self.weather_sun.setText(f"""
SUN

"Sunrise: {resource.json()[item]['sunrise']}
"Sunset: {resource.json()[item]['sunset']}""")

    def show_weather_5(self, resource):
        if self.option != 0:
            self._remove_QLabels()
            self.option = 0
        days = []
        for i in resource['list']:
            if ("15:00:00") in i['dt_txt']:
                days.append(f"{i['dt_txt']:10}, {int(i['main']['temp'])}, {i['weather'][0]['description']}")
        self.weather.setText("\n\n".join(map(str, days))) 


def main_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main_window()        