import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([1.2, 3.5, 4.7, 5.0])

# Call the torch.round function to round the elements of the tensor
rounded_tensor = torch.round(tensor)

print("Original Tensor:", tensor)
print("Rounded Tensor:", rounded_tensor)