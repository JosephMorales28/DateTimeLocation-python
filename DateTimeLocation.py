from datetime import datetime, date
from pytz import timezone
from geopy.geocoders import Nominatim

# Getting Current date
today = date.today()
print("Today's date:", today)

# Get current time in Manila, Philippines
manila_tz = timezone('Asia/Manila')
manila_time = datetime.now(manila_tz)
print("Current time in Manila, Philippines:", manila_time.time())

# Get the coordinates of Manila, Philippines
geolocator = Nominatim(user_agent="geoapiExercises")
location = geolocator.geocode("Manila, Philippines")
print("Coordinates of Manila, Philippines:", location.latitude, location.longitude)
