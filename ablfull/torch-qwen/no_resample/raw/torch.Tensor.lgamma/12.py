import torch

# Generate valid input data
input_tensor = torch.tensor([0.5, 1.0, 2.0], dtype=torch.float32)

# Call the API
result = torch.Tensor.lgamma(input_tensor)
print(result)