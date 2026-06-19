import torch

# Generate valid input data
loc = torch.tensor([0.5])
concentration = torch.tensor([1.0])

# Call the API
dist = torch.distributions.von_mises.VonMises(loc, concentration)