import torch

# Example usage of torch.ceil
input_tensor = torch.tensor([-1.7, 2.3, 0.5])
result = torch.ceil(input_tensor)
print(result)  # Output: tensor([-1.,  3.,  1.])