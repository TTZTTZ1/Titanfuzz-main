import torch

# Example usage of torch.sin
input_tensor = torch.tensor([0.0, 1.5708, 3.1416])  # Corresponds to [0, π/2, π]
output_tensor = torch.sin(input_tensor)
print(output_tensor)