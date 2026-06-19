import torch

# Prepare valid input data
input_data = 0  # Scalar value within the allowed range

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=input_data)