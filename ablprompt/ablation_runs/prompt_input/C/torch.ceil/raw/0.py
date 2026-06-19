import torch

# Create a tensor with float values
input_tensor = torch.tensor([-1.2, 3.5, -0.7, 4.0])

# Apply torch.ceil to round up each element
result_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after ceil:", result_tensor)