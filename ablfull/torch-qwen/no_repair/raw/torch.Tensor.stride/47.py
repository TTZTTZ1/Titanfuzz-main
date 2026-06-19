import torch

# Create a tensor
tensor = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])

# Call the API
result = tensor.stride()
print(result)