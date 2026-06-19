import torch

# Prepare valid input data
input1 = torch.tensor([1.0, -1.0, 0.5], dtype=torch.float)
input2 = torch.tensor([-1.0, 1.0, -0.5], dtype=torch.float)
target = torch.tensor([1, -1, 1], dtype=torch.long)

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(reduction='mean')
loss = loss_fn(input1, input2, target)

print(loss)