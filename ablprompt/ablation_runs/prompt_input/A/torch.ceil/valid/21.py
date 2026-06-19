import torch

# Example usage of torch.ceil
input_tensor = torch.tensor([-1.2, 3.5, -0.8, 2.0])
result = torch.ceil(input_tensor)
print(result)  # Output: tensor([-1.,  4., -0.,  2.])