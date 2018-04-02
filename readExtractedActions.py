import json
from google.protobuf.json_format import Parse
from s2clientprotocol import sc2api_pb2 as sc_pb

ACTION_PATH = 'parsed_replays/Actions/Terran_vs_Terran/Terran/1@02ba1de0e9e04ee3878c67e3a5d2ec206a7ca1a31c7e3e17f2cf2e7f89f07e87.SC2Replay'
SAMPLED_ACTION_PATH = 'parsed_replays/SampledActions/Terran_vs_Terran/7c3ffd7f59cae0d7ba2d2797186b3ea881db0b0cd4d04d9602f4b3eb17e61da2.SC2Replay'

with open(SAMPLED_ACTION_PATH) as f:
    actions = json.load(f)

for actions_per_frame in actions:
    for action_str in actions_per_frame:
        action = Parse(action_str, sc_pb.Action())
        print('############')
        print('action: ', action)
