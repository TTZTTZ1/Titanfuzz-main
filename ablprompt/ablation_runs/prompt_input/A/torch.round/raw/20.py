import torch

# Create a tensor with floating-point values
tensor = torch.tensor([1.2, 2.5, 3.7, 4.1])

# Call the torch.round function to round the elements of the tensor
rounded_tensor = torch.round(tensor)

print("Original Tensor:", tensor)
print("Rounded Tensor:", rounded_tensor)