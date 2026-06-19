import torch

# Create a tensor with floating-point values
input_tensor = torch.tensor([1.5, 2.3, -0.7, 4.8])

# Apply the floor function to the tensor
output_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying torch.floor:", output_tensor)