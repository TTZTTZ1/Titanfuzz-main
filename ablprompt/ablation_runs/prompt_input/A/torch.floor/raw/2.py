import torch

# Example usage of torch.floor
input_tensor = torch.tensor([2.5, 3.14, -1.7])
result = torch.floor(input_tensor)
print(result)  # Output: tensor([2., 3., -2.])