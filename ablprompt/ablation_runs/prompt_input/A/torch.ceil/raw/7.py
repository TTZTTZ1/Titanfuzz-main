import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, 3.7, -0.5, 4.0])

# Call the torch.ceil function to round up each element in the tensor
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after ceil:", output_tensor)