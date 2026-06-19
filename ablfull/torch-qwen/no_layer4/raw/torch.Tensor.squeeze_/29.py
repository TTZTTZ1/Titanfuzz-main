import torch

# Prepare valid input data
input_tensor = torch.randn(1, 1, 2, 2)

# Call the API
result = input_tensor.squeeze_()

print(result)