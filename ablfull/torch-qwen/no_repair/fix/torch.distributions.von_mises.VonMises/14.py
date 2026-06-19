
import torch
from torch.distributions import VonMises
loc = torch.tensor(0.0)
concentration = torch.tensor(1.0)
vm = VonMises(loc, concentration)
