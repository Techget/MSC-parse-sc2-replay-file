import stream
from s2clientprotocol import sc2api_pb2 as sc_pb
SAMPLED_OBSERVATION_PATH = 'parsed_replays/SampledObservations/Terran_vs_Terran/Terran/1@0008edd10656cc66b14b367400bfe5bd50ddd6bb6f5941c2921e144ef0c01f18.SC2Replay'

OBS =  [obs for obs in stream.parse(SAMPLED_OBSERVATION_PATH, sc_pb.ResponseObservation)]
print(OBS)
