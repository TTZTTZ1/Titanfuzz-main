import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])

# Initialize the Softplus layer with beta=2.0 and threshold=15.0
softplus_layer = torch.nn.Softplus(beta=2.0, threshold=15.0)

# Apply the Softplus activation function
output_tensor = softplus_layer(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)