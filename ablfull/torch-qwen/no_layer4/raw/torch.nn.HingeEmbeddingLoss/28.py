import torch

# Prepare input data
input1 = torch.randn(3)
input2 = torch.randn(3)
target = torch.tensor([1, -1, 1])

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(reduction='mean')
loss = loss_fn(input1, input2, target)

print(loss)