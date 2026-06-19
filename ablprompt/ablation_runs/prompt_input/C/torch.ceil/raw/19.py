import torch

# Create a tensor with float values
input_tensor = torch.tensor([-1.2, 3.5, -4.8, 2.1])

# Apply torch.ceil to round up the elements
result_tensor = torch.ceil(input_tensor)

print("Input Tensor:", input_tensor)
print("Result Tensor after ceil:", result_tensor)