import torch
loc = 0.0
concentration = torch.tensor(1.0)
dist = torch.distributions.von_mises.VonMises(loc, concentration)