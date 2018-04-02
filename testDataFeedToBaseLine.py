import json
from google.protobuf.json_format import Parse
from s2clientprotocol import sc2api_pb2 as sc_pb
import numpy as np
from scipy import sparse

json_path = 'train_val_test/Terran_vs_Terran/train.json'
data = json.load(open(json_path))

for da in data:
	# F = np.asarray(sparse.load_npz(da['Protoss'][1]['global_path']).todense())
	S = np.asarray(sparse.load_npz(da['Terran'][1]['spatial_path_S']).todense()).reshape([-1, 13, 64, 64])
	G = np.asarray(sparse.load_npz(da['Terran'][1]['spatial_path_G']).todense())
	action_path = da['Terran'][1]['spatial_path_G']
	action_path = action_path.replace('SpatialFeatureTensor', 'SampledActions')
	action_path = action_path[:-6] # remove the trailing '@G.npz'
	# print(action_path)
	with open(action_path) as f:
	    actions_json = json.load(f)
	#actions = [None if len(actions[idx]) == 0 else Parse(actions[idx][0], sc_pb.Action())\
	#	for idx in sampled_action_id]

	actions = []
	for actions_per_frame in actions_json:
		actions_temp = []
		for action_str in actions_per_frame:
			action = Parse(action_str, sc_pb.Action())
			actions_temp.append(action)
		actions.append(actions_temp)

	print(len(S), len(G), len(actions), '!!!!!!!!!!!!')
	for s_info,g_info,action in zip(S, G, actions):
		# feed these to baselines
		print('########')
		print(len(S), len(G), len(actions), '!!!!!!!!!!!!')
		print(s_info, g_info, action)



