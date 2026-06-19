import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, 3.7, -4.5, 0.9])

# Apply torch.floor to round down each element
result_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after Floor:", result_tensor)