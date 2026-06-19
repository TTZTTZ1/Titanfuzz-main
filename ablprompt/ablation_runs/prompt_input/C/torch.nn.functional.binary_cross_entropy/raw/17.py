import torch
import torch.nn.functional as F

# Generate random input and target tensors
input = torch.rand(3, requires_grad=True)
target = torch.randint(0, 2, (3,), dtype=torch.float)

# Compute binary cross-entropy loss
loss = F.binary_cross_entropy(input, target)

print(f"Input: {input}")
print(f"Target: {target}")
print(f"Loss: {loss}")

# Backward pass to compute gradients
loss.backward()
print(f"Gradients of input: {input.grad}")