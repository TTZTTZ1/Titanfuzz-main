import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0], dtype=torch.float32)

# Call the tan function from PyTorch
output_tensor = torch.tan(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)