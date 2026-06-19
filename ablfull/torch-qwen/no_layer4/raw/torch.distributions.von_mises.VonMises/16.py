import torch

# Prepare valid input data
loc = torch.tensor(0.0)
concentration = torch.tensor(1.5)

# Call the API
dist = torch.distributions.von_mises.VonMises(loc, concentration)