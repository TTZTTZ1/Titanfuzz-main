import torch
from torch.distributions import von_mises
loc = 0.0
concentration = torch.tensor(1.5)
vm_dist = von_mises.VonMises(loc, concentration)