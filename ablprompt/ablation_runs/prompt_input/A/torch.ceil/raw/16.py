import torch

# Create a tensor with floating-point values
input_tensor = torch.tensor([1.2, 2.5, 3.7, -0.8])

# Call the torch.ceil function to round up each element of the tensor
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ceil:", output_tensor)