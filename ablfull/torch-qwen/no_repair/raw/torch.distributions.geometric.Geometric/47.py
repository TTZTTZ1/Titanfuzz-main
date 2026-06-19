import torch

# Prepare valid input data
probs = 0.5  # Scalar probability within the valid range (0, 1]
validate_args = False  # Optional boolean parameter

# Call the API
dist = torch.distributions.Geometric(probs=probs, validate_args=validate_args)