import json
from google.protobuf.json_format import Parse
from s2clientprotocol import sc2api_pb2 as sc_pb

Name = '1@04dc996078fde09d89b18de27d7570e6077b13483f69611fbb7a93ad8e3a29e8.SC2Replay'

GLOBAL_INFO_PATH = '/parsed_replays/GlobalInfos/Terran_vs_Terran/Terran/'+Name

PATH2 = 'parsed_replays/GlobalInfos/Terran_vs_Terran/Terran/1@0553abd0df0ead191d279074ded6c426dedd5d371dded691bf44e380b92cd359.SC2Replay'


with open(PATH2) as f:
    global_info = json.load(f)
GAME_INFO = Parse(global_info['game_info'], sc_pb.ResponseGameInfo())
DATA_RAW  = Parse(global_info['data_raw'], sc_pb.ResponseData())

print(GAME_INFO)
#print(DATA_RAW)
