import torch

# Generate input data
input_tensor = torch.randn(1, 1, 2)

# Call the API
input_tensor.squeeze_()
print(input_tensor)