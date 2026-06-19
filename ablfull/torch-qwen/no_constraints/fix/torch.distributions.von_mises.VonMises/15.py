import torch
loc = torch.tensor([0.5], dtype=torch.float32)
concentration = torch.tensor([1.0], dtype=torch.float32)
dist = torch.distributions.von_mises.VonMises(loc, concentration)