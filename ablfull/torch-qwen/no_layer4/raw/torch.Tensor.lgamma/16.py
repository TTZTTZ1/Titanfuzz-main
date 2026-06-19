import torch

# Generate input data
input_tensor = torch.tensor([1.0, 2.5, 4.0])

# Call the API
result = torch.Tensor.lgamma(input_tensor)
print(result)