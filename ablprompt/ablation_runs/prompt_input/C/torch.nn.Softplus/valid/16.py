import torch

# Create an instance of Softplus with custom beta and threshold
softplus = torch.nn.Softplus(beta=0.5, threshold=15.0)

# Generate some random input data
input_data = torch.randn(3, 4)

# Apply the Softplus activation function
output_data = softplus(input_data)

print("Input Data:", input_data)
print("Output Data:", output_data)