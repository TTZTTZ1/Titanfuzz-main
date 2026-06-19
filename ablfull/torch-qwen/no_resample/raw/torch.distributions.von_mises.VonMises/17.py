import torch

# Generate valid input data
loc = torch.tensor(0.0)
concentration = torch.tensor(1.0)

# Call the API
vm = torch.distributions.von_mises.VonMises(loc, concentration)