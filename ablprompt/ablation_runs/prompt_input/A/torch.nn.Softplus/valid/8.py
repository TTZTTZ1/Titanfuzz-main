import torch

# Create an instance of Softplus
softplus = torch.nn.Softplus(beta=1, threshold=20)

# Example input tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0])

# Apply Softplus to the input tensor
output_tensor = softplus(input_tensor)

print(output_tensor)