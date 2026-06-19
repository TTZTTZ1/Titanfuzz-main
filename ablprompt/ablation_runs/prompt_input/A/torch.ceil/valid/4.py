import torch

# Create a tensor with floating-point numbers
input_tensor = torch.tensor([1.2, 2.5, 3.7, -0.4])

# Call torch.ceil to round up each element of the tensor
result_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after ceil:", result_tensor)