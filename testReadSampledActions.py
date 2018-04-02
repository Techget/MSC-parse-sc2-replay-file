import stream
from s2clientprotocol import sc2api_pb2 as sc_pb

PATH = 'parsed_replays/SampledActions/Terran_vs_Terran/Terran/7cc6fe85694768dbab7987344196ab44615842bd896f9172ee1177a2b899ba58.SC2Replay'

# OBS =  [obs for obs in stream.parse(PATH), sc_pb.ResponseObservation)]
# print(OBS)

for obs in stream.parse(PATH):
	print(sc_pb.ResponseObservation(obs))


