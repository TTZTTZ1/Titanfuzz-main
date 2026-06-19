import torch

# Prepare input data
input1 = torch.tensor([1.0, -1.0], dtype=torch.float)
target = torch.tensor([1, -1], dtype=torch.long)

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')
loss = loss_fn(input1, target)

print(loss)