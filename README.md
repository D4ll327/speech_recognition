# speech_recognition
### if you on linux system you need to download pip 
```
sudo apt-get install python-pip
```
## first we need to install 

### 1. speech_recognition
```
pip install SpeechRecognition
```

And to quickly try it out, run python -m speech_recognition after installing.

- [More info](https://pypi.python.org/pypi/SpeechRecognition/)  
### 2. pyttsx3
```
pip install pyttsx3
```

Fixes for possible errors:

No module named win32com.client

No module named win32

No module named win32api
run this
```
pip install pypiwin32
```

### 3. phue 
```
pip install phue
```
```
b = Bridge('ip_of_your_bridge')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

# Get the bridge state (This returns the full dictionary that you can explore)
b.get_api()

# Prints if light 1 is on or not
b.get_light(1, 'on')

# Set brightness of lamp 1 to max
b.set_light(1, 'bri', 254)

# Set brightness of lamp 2 to 50%
b.set_light(2, 'bri', 127)

# Turn lamp 2 on
b.set_light(2,'on', True)

# You can also control multiple lamps by sending a list as lamp_id
b.set_light( [1,2], 'on', True)

# Get the name of a lamp
b.get_light(1, 'name')

# You can also use light names instead of the id
b.get_light('Kitchen')
b.set_light('Kitchen', 'bri', 254)

# Also works with lists
b.set_light(['Bathroom', 'Garage'], 'on', False)

# The set_light method can also take a dictionary as the second argument to do more fancy stuff
# This will turn light 1 on with a transition time of 30 seconds
command =  {'transitiontime' : 300, 'on' : True, 'bri' : 254}
b.set_light(1, command
````
- [More info] https://github.com/studioimaginaire/phue

## All the language that support
| Language-Country | Language-Country Code |
| -------------    | -------------         |
| Catalan - Spain  |ca-ES |
| Content Cell     |ca-ES |
| Danish - Denmark |da-Dk |
|German - Germany | de-DE|
|English - Australia | en-AU|
|English - Canada | en-CA|
|English - Great Britain | en-GB|
|English - Indian | en-IN|
|English - United States | en-US|
|Spanish - Spain | es-ES|
|Spanish - Mexico | es-MX|
|Finnish - Finland | fi-FI|
|French - Canada | fr-CA|
|French - France | fr-FR|
|Italian - Italy | it-IT|
|Japanese - Japan | ja-JP|
|Korean - Korea | ko-KR|
|Norwegian - Norway | nb-NO|
|Dutch - Netherlands | nl-NL|
|Polish - Poland | pl-PL|
|Portuguese - Brazil | pt-BR|
|Portuguese - Portugal | pt-PT|
|Russian - Russia | ru-RU|
|Swedish - Sweden | sv-SE|
|Chinese - China | zh-CN|
|Chinese - Hong Kong | zh-HK|
|Chinese - Taiwan | zh-TW|

