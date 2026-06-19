import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Call the tan function from torch
output_tensor = torch.tan(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying tan:", output_tensor)