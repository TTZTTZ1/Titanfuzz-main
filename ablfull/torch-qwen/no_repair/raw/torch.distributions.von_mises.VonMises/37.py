import torch
from torch.distributions import VonMises

# Generate valid input data
loc = torch.tensor(0.0)
concentration = torch.tensor(1.0)

# Call the API
vm = VonMises(loc, concentration)