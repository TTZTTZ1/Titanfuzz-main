import torch

# Prepare input data
input1 = torch.tensor([1.0, -1.0], dtype=torch.float32)
input2 = torch.tensor([-1.0, 1.0], dtype=torch.float32)
target = torch.tensor([1.0, -1.0], dtype=torch.float32)

# Create an instance of HingeEmbeddingLoss
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')

# Compute the loss
loss = criterion(input1, input2, target)

print(loss)