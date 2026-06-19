import torch

# Generate a random tensor as input
input_tensor = torch.randn(3, 4, 5)

# Call the API with the required parameters
result = input_tensor.float(memory_format=torch.channels_last)