import torch

# Create an instance of Softplus with custom beta and threshold
softplus = torch.nn.Softplus(beta=0.5, threshold=10.0)

# Define a random input tensor
input_tensor = torch.randn(3, 4)

# Apply the Softplus activation function
output_tensor = softplus(input_tensor)

print("Input Tensor:")
print(input_tensor)
print("\nOutput Tensor after Softplus Activation:")
print(output_tensor)