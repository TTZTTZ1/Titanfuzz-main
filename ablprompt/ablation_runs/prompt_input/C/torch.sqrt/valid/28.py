import torch

# Create a tensor with both positive and negative values
input_tensor = torch.tensor([-4.0, -1.0, 0.0, 1.0, 4.0], dtype=torch.float32)

# Compute the square root using torch.sqrt
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)