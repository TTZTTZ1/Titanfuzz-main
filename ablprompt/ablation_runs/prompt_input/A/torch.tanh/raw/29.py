import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply tanh function
output_tensor = torch.tanh(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after tanh:", output_tensor)