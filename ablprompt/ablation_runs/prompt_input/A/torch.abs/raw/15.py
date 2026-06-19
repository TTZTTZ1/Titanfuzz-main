import torch

# Example usage of torch.abs
input_tensor = torch.tensor([-1.0, 2.0, -3.0])
abs_tensor = torch.abs(input_tensor)
print(abs_tensor)  # Output: tensor([1., 2., 3.])