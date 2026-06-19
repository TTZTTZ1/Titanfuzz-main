import torch

# Example usage of torch.cos
input_tensor = torch.tensor([0.0, 1.0, 2.0], dtype=torch.float32)
output_tensor = torch.cos(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)