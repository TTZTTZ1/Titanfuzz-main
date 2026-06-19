import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([1.2, 3.7, -2.5, 4.4])

# Call the torch.round function to round the elements of the tensor
rounded_tensor = torch.round(tensor)

print("Original Tensor:", tensor)
print("Rounded Tensor:", rounded_tensor)