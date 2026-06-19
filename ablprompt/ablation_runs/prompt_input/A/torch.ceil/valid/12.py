import torch

# Create a tensor with floating-point values
input_tensor = torch.tensor([1.2, 3.5, -0.7, 4.8])

# Call the torch.ceil function to apply ceiling operation
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Ceiling:", output_tensor)