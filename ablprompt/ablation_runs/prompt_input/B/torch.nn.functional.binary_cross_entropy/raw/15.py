import torch

# Generate random input and target tensors
input_tensor = torch.rand(3, requires_grad=True)
target_tensor = torch.randint(0, 2, (3,), dtype=torch.float)

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input_tensor, target_tensor, reduction='mean')

# Print the loss
print("Binary Cross-Entropy Loss:", loss.item())

# Backward pass to compute gradients
loss.backward()
print("Gradients of input tensor:", input_tensor.grad)