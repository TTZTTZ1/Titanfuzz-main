import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, -3.7, 4.5, -6.8])

# Apply torch.floor to the tensor
result_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after floor operation:", result_tensor)