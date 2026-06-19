import torch
from torch.nn import Sigmoid

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Sigmoid function
sigmoid_function = Sigmoid()
output_tensor = sigmoid_function(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after Sigmoid:", output_tensor)