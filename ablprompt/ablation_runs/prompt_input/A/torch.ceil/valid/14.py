import torch

# Example usage of torch.ceil
input_tensor = torch.tensor([-1.7, -1.5, -0.2, 0.3, 1.8])
result = torch.ceil(input_tensor)
print(result)  # Output: tensor([-1., -1., -0.,  1.,  2.])