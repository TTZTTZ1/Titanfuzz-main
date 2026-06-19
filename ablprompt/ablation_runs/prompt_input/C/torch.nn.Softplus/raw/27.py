import torch

# Create a Softplus layer with default parameters
softplus = torch.nn.Softplus()

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply the Softplus function
output_tensor = softplus(input_tensor)

print("Input:", input_tensor)
print("Output:", output_tensor)