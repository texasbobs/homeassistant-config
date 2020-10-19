brightness = data.get("brightness")
screen_time = data.get("screen_time")
fully_command = data.get("cmd")
motion_sen = data.get("motion_sen")
motion_on = data.get("motion_on")
acoustic_sen = data.get("acoustic_sen")
acoustic_on = data.get("acoustic_on")
dark_off = data.get("dark_off")
dark_threshold = data.get("dark_threshold")
new_url = data.get("new_url")

opened = data.get("opened")
triggered = data.get("triggered")
disarmed = data.get("disarmed")
home = data.get("home")
away = data.get("away")

start_url = True
# Play a sound  
# might add setAudioVolume&level=100&stream=1 to set levels differently

if triggered is not None:
    service_data = {"ip": 26, "cmd": "playSound&url=file%3A%2F%2F%2Fstorage%2Femulated%2F0%2FRingtones%2Ftng_red_alert3.mp3&loop=true"}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)
    service_data = {"ip": 27, "cmd": "playSound&url=file%3A%2F%2F%2Fstorage%2Femulated%2F0%2FRingtones%2Ftng_red_alert3.mp3&loop=true"}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)
    start_url = False    

if opened is not None:
    service_data = {"ip": 26, "cmd": "playSound&url=file%3A%2F%2F%2Fstorage%2Femulated%2F0%2FRingtones%2Finput_ok_3_clean.mp3&loop=false"}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)
    service_data = {"ip": 27, "cmd": "playSound&url=file%3A%2F%2F%2Fstorage%2Femulated%2F0%2FRingtones%2Finput_ok_3_clean.mp3&loop=false"}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)    
    start_url = False

if disarmed is not None: #Sending a non-looping sound in case the alarm was previously triggered. TTS will not stop a playSound that is looping.
    service_data = {"ip": 26, "cmd": "playSound&url=file%3A%2F%2F%2Fstorage%2Femulated%2F0%2FRingtones%2Finput_ok_3_clean.mp3&loop=false"}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)
    service_data = {"ip": 27, "cmd": "playSound&url=file%3A%2F%2F%2Fstorage%2Femulated%2F0%2FRingtones%2Finput_ok_3_clean.mp3&loop=false"}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)        
    service_data = {"ip": 26, "cmd": "textToSpeech&text=The+Alarm+Has+Been+Disarmed"}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)
    start_url = False

if home is not None:
    service_data = {"ip": 26, "cmd": "textToSpeech&text=The+House+Alarm+Has+Been+armed.++goodnight."}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)
    start_url = False

if away is not None:
    service_data = {"ip": 26, "cmd": "textToSpeech&text=The+House+Alarm+Has+Been+armed.+You+have+sixty+seconds+to+exit."}
    hass.services.call("rest_command", "kiosk_play_sound", service_data, False)
    start_url = False

# Screen Brightness
if brightness is not None:
    service_data = {"cmd": "setStringSetting", "key": "screenBrightness", "value": brightness}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
#Screen Time On
if screen_time is not None:
    service_data = {"cmd": "setStringSetting", "key": "timeToScreenOffV2", "value": screen_time}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
#Send a command to fully
if fully_command is not None:
    service_data = {"cmd": fully_command}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
# Motion Sensitivity
if motion_sen is not None:
    service_data = {"cmd": "setStringSetting", "key": "motionSensitivity", "value": motion_sen}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
# Motion Activate
if motion_on is not None:
    service_data = {"cmd": "setBooleanSetting", "key": "motionDetection", "value": motion_on}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
# Acoustic Activate
if acoustic_on is not None:
    service_data = {"cmd": "setBooleanSetting", "key": "motionDetectionAcoustic", "value": acoustic_on}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
# Acoustic Sensitivity
if acoustic_sen is not None:
    service_data = {"cmd": "setStringSetting", "key": "motionSensitivityAcoustic", "value": acoustic_sen}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
# Screen turns off with darkness
if dark_off is not None:
    service_data = {"cmd": "setBooleanSetting", "key": "screenOffInDarkness", "value": dark_off}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
# Darkness threshold
if dark_threshold is not None:
    service_data = {"cmd": "setStringSetting", "key": "darknessLevel", "value": dark_threshold}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
# Load new URL
if new_url is not None:
    service_data = {"cmd": "loadUrl", "url": new_url}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    start_url = False
# If no data is entered at all the the start URL is loaded
if start_url is True:
    service_data = {"cmd": "loadStartUrl"}
    hass.services.call("rest_command", "kiosk_command", service_data, False)
    logger.info("Fully Kiosk Test Variable")
