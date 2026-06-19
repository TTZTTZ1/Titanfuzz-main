import torch

# Step 2: Generate valid input data
probs = torch.tensor(0.5)

# Step 3: Call the API
torch.distributions.Geometric(probs=probs)