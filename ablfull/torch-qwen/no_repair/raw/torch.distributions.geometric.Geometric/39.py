import torch

# Generate input data
probs = torch.tensor(0.5)
logits = None
validate_args = False

# Call the API
result = torch.distributions.geometric.Geometric(probs=probs, logits=logits, validate_args=validate_args)