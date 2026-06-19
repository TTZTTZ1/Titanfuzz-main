
import torch
loc = torch.tensor(0.0)
concentration = torch.tensor(1.0)
distribution = torch.distributions.von_mises.VonMises(loc, concentration)
