import torch

# Prepare input data
input_data = 0  # Valid scalar value within the specified range

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=input_data)