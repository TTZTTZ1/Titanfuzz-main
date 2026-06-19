import torch
loc = torch.tensor(0.5)
concentration = torch.tensor(2.0)
von_mises_dist = torch.distributions.von_mises.VonMises(loc, concentration)