import torch

# Create a tensor with floating-point values
input_tensor = torch.tensor([1.2, 2.5, -0.3])

# Call torch.ceil to compute the ceiling of each element in the tensor
output_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Ceiling:", output_tensor)