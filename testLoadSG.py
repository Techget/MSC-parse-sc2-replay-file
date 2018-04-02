import numpy as np
from scipy import sparse
PATH1 = 'parsed_replays/surveillance.idealtest.org/parsed_replays/SpatialFeatureTensor/Protoss_vs_Protoss/Protoss/1@003c24178914596dc2701174fe6112705cd06c795563eb3bad4bc05650dc9bd0.SC2Replay@S.npz'
PATH2 = 'parsed_replays/surveillance.idealtest.org/parsed_replays/SpatialFeatureTensor/Protoss_vs_Protoss/Protoss/1@003c24178914596dc2701174fe6112705cd06c795563eb3bad4bc05650dc9bd0.SC2Replay@G.npz'

S = np.asarray(sparse.load_npz(PATH1).todense()).reshape([-1, 13, 64, 64])
# print(S)
#for s in S:
#	print(s[0:8,:,:])
#	print(s[]
	


G = np.asarray(sparse.load_npz(PATH2).todense())
for g in G:
	print(g[24], g[25])

