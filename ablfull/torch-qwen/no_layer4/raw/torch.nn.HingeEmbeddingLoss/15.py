import torch

# Prepare input data
input1 = torch.tensor([1.0, -1.0])
input2 = torch.tensor([-1.0, 1.0])
target = torch.tensor([1.0, -1.0])

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(reduction='mean')
loss = loss_fn(input1, input2, target)
print(loss)