import torch

# Generate a tensor of shape (3,) with values between 0 and 1
input_tensor = torch.rand(3)

# Call the API
result = input_tensor.bernoulli_()