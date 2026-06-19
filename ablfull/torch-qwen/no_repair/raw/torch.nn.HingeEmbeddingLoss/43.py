import torch

# Prepare input data
input1 = torch.randn(5)
input2 = torch.randn(5)
target = torch.randint(0, 2, (5,), dtype=torch.long)

# Create the HingeEmbeddingLoss instance
loss_fn = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')

# Compute the loss
loss = loss_fn(input1, input2, target)
print(loss.item())