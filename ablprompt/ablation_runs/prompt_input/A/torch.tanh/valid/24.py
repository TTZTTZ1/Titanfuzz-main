import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the tanh function to the tensor
output_tensor = torch.tanh(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after tanh:", output_tensor)