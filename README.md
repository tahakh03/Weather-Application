# Project Overview

This project is a Weather Application built using Python's Tkinter for the GUI and integrates with OpenWeatherMap API to fetch current weather data based on user-entered city names.

## Project Features

- **Real-time Weather Data**: Fetches current weather conditions including temperature, wind speed, humidity, pressure, and weather description.
   
- **User-Friendly Interface**: Utilizes Tkinter for a graphical user interface that allows users to easily input city names and retrieve weather information.

- **Visual Representation**: Displays weather data with clear labels and icons for easy interpretation.

## Project Components

1. **Scraping and API Integration**: Utilizes `requests` and `json` modules to fetch weather data from the OpenWeatherMap API.

2. **GUI Development**: Built with Tkinter to create a responsive and visually appealing user interface.

3. **Data Display**: Displays weather information including temperature in Celsius, weather condition, wind speed, humidity percentage, and atmospheric pressure.

## Files and Structure

### Files

- `weather.py`: Main script that contains the Tkinter GUI setup and weather data retrieval logic.
- `searchbox.png`: Image file for the search box icon in the GUI.
- `searchicon.png`: Image file for the search icon button in the GUI.
- `logo.png`: Image file for the logo displayed in the GUI.
- `display_box.png`: Image file for the bottom display box in the GUI.

### Dependencies

- `tkinter`: Python's standard GUI (graphical user interface) package.
- `requests`: HTTP library for making API requests.
- `timezonefinder`: Library to find the timezone of a location based on latitude and longitude.
- `pytz`: World timezone definitions and daylight saving time (DST) calculations.
