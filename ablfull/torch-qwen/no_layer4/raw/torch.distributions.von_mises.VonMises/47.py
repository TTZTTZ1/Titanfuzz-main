import torch

# Task 2: Generate input data
loc = torch.tensor(0.5)
concentration = torch.tensor(2.0)

# Task 3: Call the API
von_mises_dist = torch.distributions.von_mises.VonMises(loc, concentration)