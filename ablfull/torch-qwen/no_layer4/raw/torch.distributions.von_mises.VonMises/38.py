import torch
from torch.distributions import von_mises

# Generate input data
loc = torch.tensor(0.5)
concentration = torch.tensor(1.0)

# Call the API
distribution = von_mises.VonMises(loc, concentration)