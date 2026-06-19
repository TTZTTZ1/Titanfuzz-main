import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Call the torch.exp function
output_tensor = torch.exp(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)