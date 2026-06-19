import torch

# Prepare valid input data
loc = torch.tensor(0.0)
concentration = torch.tensor(1.0)

# Call the API
von_mises_distribution = torch.distributions.von_mises.VonMises(loc, concentration)