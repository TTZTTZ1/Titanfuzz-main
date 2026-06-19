import torch

# Create an instance of LeakyReLU with a negative slope of 0.1
leaky_relu = torch.nn.LeakyReLU(negative_slope=0.1)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply LeakyReLU to the input tensor
output_tensor = leaky_relu(input_tensor)

print(output_tensor)