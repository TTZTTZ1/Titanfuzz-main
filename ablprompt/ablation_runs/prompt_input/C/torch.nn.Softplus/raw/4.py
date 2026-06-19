import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Initialize Softplus with beta=3.0 and threshold=15.0
softplus = torch.nn.Softplus(beta=3.0, threshold=15.0)

# Apply Softplus to the input tensor
output_tensor = softplus(input_tensor)

print(output_tensor)