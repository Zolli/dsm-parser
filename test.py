from dsmr_parser import telegram_specifications
from dsmr_parser.clients import SocketReader
import os

socket_reader = SocketReader(
    host='172.10.10.51',
    port=23,
    telegram_specification=telegram_specifications.SWEDEN
)

#for telegram in socket_reader.read():
#    print(telegram)  # see 'Telegram object' docs below

for telegram in socket_reader.read_as_object():
    os.system('clear')
    print(telegram)
