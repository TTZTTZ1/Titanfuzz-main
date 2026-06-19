import torch

# Example usage of torch.ceil
input_tensor = torch.tensor([-1.5, 2.3, -0.7, 4.0])
result = torch.ceil(input_tensor)
print(result)  # Output: tensor([-1.,  3., -0.,  4.])