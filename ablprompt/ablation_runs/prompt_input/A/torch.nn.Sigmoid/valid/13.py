import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Sigmoid function
sigmoid_function = torch.nn.Sigmoid()
output_tensor = sigmoid_function(input_tensor)

print(output_tensor)