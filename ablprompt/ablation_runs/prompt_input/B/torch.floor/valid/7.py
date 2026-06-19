import torch

# Create a random tensor
input_tensor = torch.tensor([1.5, -2.3, 4.7, -0.8], dtype=torch.float32)

# Apply torch.floor to the tensor
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after floor:", output_tensor)