import torch
from torch.autograd import Variable

# Create random input and target tensors
input = Variable(torch.rand(3, 5))
target = Variable(torch.randint(0, 2, (3, 5)).float())

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input, target)

print(loss)