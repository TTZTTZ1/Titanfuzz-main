import torch

loc = 0.0
concentration = torch.tensor(1.5)

dist = torch.distributions.von_mises.VonMises(loc, concentration)