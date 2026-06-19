import torch

# Prepare valid input data
input_data = 0  # cache_size must be either 0 or 1

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=input_data)