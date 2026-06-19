import torch

loc = 0.0
concentration = 1.5
von_mises_dist = torch.distributions.von_mises.VonMises(loc, concentration)