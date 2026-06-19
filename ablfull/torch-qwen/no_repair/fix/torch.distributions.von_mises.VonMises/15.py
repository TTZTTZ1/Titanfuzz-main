
import torch
loc = torch.tensor(0.5)
concentration = torch.tensor(1.0)
vm_dist = torch.distributions.von_mises.VonMises(loc, concentration)
