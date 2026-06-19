import torch

# Create a tensor
input_tensor = torch.tensor([-1.0, 0.0, 1.0, 2.0])

# Initialize Softplus with custom beta and threshold
softplus = torch.nn.Softplus(beta=2.0, threshold=30.0)

# Apply Softplus to the input tensor
output_tensor = softplus(input_tensor)

print("Input Tensor:", input_tensor)
print("Output Tensor:", output_tensor)