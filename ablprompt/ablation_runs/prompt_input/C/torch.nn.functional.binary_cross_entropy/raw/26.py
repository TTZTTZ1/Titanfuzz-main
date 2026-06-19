import torch
import torch.nn.functional as F

# Example input and target tensors
input_tensor = torch.tensor([[0.1, 0.4, 0.3], [0.8, 0.2, 0.5]], requires_grad=True)
target_tensor = torch.tensor([[0, 1, 0], [1, 0, 1]])

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input_tensor, target_tensor)

# Print the loss
print(loss)

# Backward pass to compute gradients
loss.backward()
print(input_tensor.grad)