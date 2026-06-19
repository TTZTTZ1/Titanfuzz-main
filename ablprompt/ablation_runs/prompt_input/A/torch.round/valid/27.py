import torch

# Create a tensor with floating-point values
tensor = torch.tensor([1.2, 2.5, 3.7, 4.4])

# Call the torch.round function to round the tensor elements
rounded_tensor = torch.round(tensor)

# Print the original and rounded tensors
print("Original Tensor:", tensor)
print("Rounded Tensor:", rounded_tensor)