import torch
from torch.autograd import Variable

# Create random input and target tensors
input_tensor = Variable(torch.randn(3, requires_grad=True))
target_tensor = Variable(torch.randint(0, 2, (3,), dtype=torch.float))

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input_tensor, target_tensor)

print("Input Tensor:", input_tensor.data)
print("Target Tensor:", target_tensor.data)
print("Computed Loss:", loss.item())