import torch
from torch.distributions import von_mises
loc = torch.tensor(0.5)
concentration = torch.tensor(1.0)
distribution = von_mises.VonMises(loc, concentration)