import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([2.5, -1.3, 4.8, -0.7])

# Apply torch.floor to the tensor
result_tensor = torch.floor(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after applying torch.floor:", result_tensor)