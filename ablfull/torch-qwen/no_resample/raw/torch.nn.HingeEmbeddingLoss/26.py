import torch

# Prepare input data
input1 = torch.tensor([1.0, -1.0], requires_grad=True)
input2 = torch.tensor([-1.0, 1.0], requires_grad=True)
target = torch.tensor([1, -1])

# Create loss function instance
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')

# Compute loss
loss = criterion(input1, input2, target)

print(loss)