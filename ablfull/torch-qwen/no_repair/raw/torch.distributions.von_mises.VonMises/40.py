import torch

# Prepare input data
loc = torch.tensor(0.5)
concentration = torch.tensor(1.0)

# Call the API
vm_dist = torch.distributions.von_mises.VonMises(loc, concentration)