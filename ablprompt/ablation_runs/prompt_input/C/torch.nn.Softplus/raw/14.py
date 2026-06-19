import torch

# Create a tensor with random values
input_tensor = torch.randn(5, 5)

# Initialize the Softplus layer with custom beta and threshold
softplus = torch.nn.Softplus(beta=2.0, threshold=30.0)

# Apply the Softplus activation function
output_tensor = softplus(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nOutput Tensor after Softplus Activation:")
print(output_tensor)