import torch

# Create an instance of LeakyReLU
leaky_relu = torch.nn.LeakyReLU(negative_slope=0.01)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply LeakyReLU activation
output_tensor = leaky_relu(input_tensor)

print(output_tensor)