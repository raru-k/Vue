import smbus
import time
import sys
import iothub_client

from iothub_client import IoTHubClient, IoTHubClientError, IoTHubTransportProvider, IoTHubClientResult
from iothub_client import IoTHubMessage, IoTHubMessageDispositionResult, IoTHubError, DeviceMethodReturnValue

CONNECTION_STRING = "HostName=IoTHubRaiki.azure-devices.net;DeviceId=RaspberryPi;SharedAccessKey=oESxTToZUukYLO1k5dnwnHfsMddh6FS2kkv3ZVd0TfQ="
PROTOCOL = IoTHubTransportProvider.MQTT
MSG_TXT = "{\"temperature\": %.2f}"
bus = smbus.SMBus(1)
    
def send_confirmation_callback(message, result, user_context):
    print("IoT Hub responded to message with status %s" % (result))
    
def iothub_client_init():
    client = IoTHubClient(CONNECTION_STRING, PROTOCOL)
    return client

def adt7410():
    block = bus.read_i2c_block_data(0x48, 0x00, 2)
    data = (block[0] << 8 | block[1] )>> 3
    if ( data >= 4096):
        data -= 8192
    
    temp = data * 0.0625
    return temp

try:
    client = iothub_client_init()
    while True:
        inputValue = adt7410()
        msg_txt_formatted = MSG_TXT % (inputValue)
        message = IoTHubMessage(msg_txt_formatted)
        client.send_event_async(message, send_confirmation_callback, None)
        time.sleep(1)

except KeyboardInterrupt:
    pass
