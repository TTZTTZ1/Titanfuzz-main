import torch

# Example usage of torch.abs
input_tensor = torch.tensor([-1.0, 2.0, -3.0])
absolute_values = torch.abs(input_tensor)
print(absolute_values)  # Output: tensor([1., 2., 3.])