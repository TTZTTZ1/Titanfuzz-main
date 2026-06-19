import torch

loc = torch.tensor(0.0)
concentration = torch.tensor(1.5)

von_mises_distribution = torch.distributions.von_mises.VonMises(loc, concentration)