import torch

# Step 2: Generate input data
p = torch.tensor([0.5])

# Step 3: Call the API
result = torch.Tensor().bernoulli_(p)