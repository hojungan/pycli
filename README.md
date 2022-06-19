# Pycli
CLI tool created using Python and Click  

## Commands
### Weather
Uses OpenWeatherMap API to grab the current weather of the specified city  

**Command**  
`pycli weather [city]`

### Config
To store API key to use the OpenWeatherMap  
To create the API key, go to [OpenWeatherMap]("https://openweathermap.org/api")  
Sign up and create API key for `Current Weather Data`  
Run `pycli config add --help` for more information  

**Command**  
`pycli config add --api-key [apikey]`  