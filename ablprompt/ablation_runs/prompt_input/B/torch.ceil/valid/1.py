import torch

# Create a tensor with both integer and float values
input_tensor = torch.tensor([-1.2, -0.5, 0.3, 1.7, 2])

# Apply torch.ceil to the tensor
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)