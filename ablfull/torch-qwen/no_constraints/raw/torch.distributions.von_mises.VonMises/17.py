import torch

# Task 2: Generate input data
loc = torch.tensor([0.5])
concentration = torch.tensor([1.0])

# Task 3: Call the API
vm = torch.distributions.von_mises.VonMises(loc, concentration)