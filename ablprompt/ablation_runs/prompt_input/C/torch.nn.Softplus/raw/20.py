import torch

# Create a tensor with random values
input_tensor = torch.randn(3, 4)

# Initialize the Softplus layer with beta=2 and threshold=15
softplus_layer = torch.nn.Softplus(beta=2, threshold=15)

# Apply the Softplus activation function to the input tensor
output_tensor = softplus_layer(input_tensor)

print(output_tensor)