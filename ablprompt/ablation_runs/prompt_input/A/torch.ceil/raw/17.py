import torch

# Example usage of torch.ceil
input_tensor = torch.tensor([-1.7, -1.5, -0.2, 0.3, 1.5, 2.1])
output_tensor = torch.ceil(input_tensor)
print(output_tensor)