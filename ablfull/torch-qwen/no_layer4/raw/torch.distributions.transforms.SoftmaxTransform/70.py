import torch

# Prepare input data
input_data = torch.tensor(0)

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=input_data.item())