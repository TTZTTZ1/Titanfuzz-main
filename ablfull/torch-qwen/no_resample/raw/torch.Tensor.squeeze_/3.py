import torch

# Prepare input data
input_tensor = torch.randn(1, 1, 3, 4)

# Call the API
result = input_tensor.squeeze_()
print(result)