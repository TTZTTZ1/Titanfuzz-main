import torch
from torch.autograd import Variable

# Create random input and target tensors
input_tensor = Variable(torch.rand(3, 5))
target_tensor = Variable(torch.randint(0, 2, (3, 5)).float())

# Compute binary cross-entropy loss
loss = torch.nn.functional.binary_cross_entropy(input_tensor, target_tensor)

print("Computed Loss:", loss.item())