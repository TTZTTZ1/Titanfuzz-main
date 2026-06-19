import torch

# Prepare valid input data
probs = torch.tensor(0.7)
logits = None

# Call the API
dist = torch.distributions.geometric.Geometric(probs=probs, logits=logits, validate_args=False)