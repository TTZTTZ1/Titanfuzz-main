import torch

# Create a random tensor with values between -5 and 5
input_tensor = torch.rand(3, 3) * 10 - 5

# Compute the exponential of each element in the tensor
output_tensor = torch.exp(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after applying exp:")
print(output_tensor)