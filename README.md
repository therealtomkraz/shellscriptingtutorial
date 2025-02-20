
## Documentation

This repository contains a collection of Bash scripts designed to demonstrate practical applications of shell scripting. These scripts cover various tasks from weather fetching to file organization, showcasing different aspects of Bash scripting. Scripts Overview

## Weather Fetcher

**File:** weather_fetcher.sh

This script fetches current weather data for a specified city using the Open-Meteo API.

**Features:**

* Retrieves geographic coordinates for a given city name
* Fetches current weather data (temperature, wind speed, humidity)
* Displays formatted weather information

**Usage:**

    bash ./weather_fetcher.sh [city name]

## Geo-Location Finder

**File:** geo_finder.sh

This script retrieves latitude, longitude, and other geographic information for a specified city using the Open-Meteo Geocoding API.

**Features:**

* Fetches geographic data for a given city name
* Displays city name, latitude, longitude, country, and timezone

**Usage:**

    bash ./geo_finder.sh [city name]

## Task Tracker

**File:** task_tracker.sh

A simple task management script that allows users to add, list, and manage tasks.

**Features:**

* Add new tasks
* List existing tasks
* Mark tasks as complete
* Todo: Remove tasks

**Usage:**

    bash ./task_tracker.sh

## File Organizer

**File:** file_organizer.sh

This script organizes files in a specified directory by moving them into categorized folders based on their file extensions.

**Features:**

* Categorizes files into Images, Documents, and Archives
* Creates category folders if they don't exist
* Moves files to appropriate folders based on extension

**Usage:**

bash ./file_organizer.sh [directory path]

**Requirements**
* Bash shell
* curl for API requests
* jq for JSON parsing (in weather and geo-location scripts)

## Create 1000 random files. 

**File:** file_organizer.sh

This script creates 1000 random files in a directory. 

**Features:**

* Creates 100 random files.
* Types are Images, Documents, and Archives
* Creates a folders if they don't exist
* Files are of random size, all under 1k.

**Usage:**

bash ./file_organizer.sh [directory path]

**Requirements**
* Bash shell
* python3
* pythone module "random_word"


**Installation**

Clone this repository:

    git clone https://github.com/yourusername/bash-scripting-utilities.git

Navigate to the script directory:

    cd bash-scripting-utilities

Make the scripts executable:

    chmod +x *.sh

    

## Contributing

Contributions to improve the scripts or add new utilities are welcome. Please feel free to submit a pull request or open an issue for any bugs or feature requests. 

## License

This project is open source and available under the MIT License.



