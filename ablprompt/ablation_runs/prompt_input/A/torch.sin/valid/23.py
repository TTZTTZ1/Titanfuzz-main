import torch

# Example usage of torch.sin
input_tensor = torch.tensor([0.0, 1.5708, 3.1416])  # Corresponds to [0, pi/2, pi]
output_tensor = torch.sin(input_tensor)
print(output_tensor)