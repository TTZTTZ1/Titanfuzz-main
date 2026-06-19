import torch

# Create a tensor with some values
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the Sigmoid function
sigmoid_function = torch.nn.Sigmoid()
output_tensor = sigmoid_function(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor after applying Sigmoid:", output_tensor)