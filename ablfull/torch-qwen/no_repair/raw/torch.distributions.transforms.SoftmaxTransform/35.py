import torch

# Prepare valid input data
input_data = 0

# Call the target API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=input_data)