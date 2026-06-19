import torch

# Create a tensor with floating-point numbers
tensor = torch.tensor([1.2, 2.5, 3.7, 4.4])

# Call torch.round to round the elements of the tensor to the nearest integer
rounded_tensor = torch.round(tensor)

print("Original Tensor:", tensor)
print("Rounded Tensor:", rounded_tensor)