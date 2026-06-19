import torch

# Example usage of torch.ceil
input_tensor = torch.tensor([-1.7, -1.5, -0.2, 0.3, 1.8, 2.1])
result = torch.ceil(input_tensor)
print(result)  # Output should be tensor([-1., -1., -0.,  1.,  2.,  3.])