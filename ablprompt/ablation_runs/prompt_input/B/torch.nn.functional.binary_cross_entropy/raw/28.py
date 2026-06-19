import torch
from torch.autograd import Variable

# Create random input and target tensors
input = Variable(torch.randn(3, requires_grad=True))
target = Variable(torch.empty(3).random_(2))

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input, target)

print('Input:', input.data)
print('Target:', target.data)
print('Loss:', loss.data)