import torch

# Create a random tensor with negative and positive values
input_tensor = torch.tensor([-1.0, 4.0, 9.0], dtype=torch.float32)

# Compute the square root using torch.sqrt
output_tensor = torch.sqrt(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)