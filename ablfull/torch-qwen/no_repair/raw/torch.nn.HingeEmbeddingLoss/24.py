import torch

# Prepare valid input data
input1 = torch.tensor([1.0, -1.0, 0.5], requires_grad=True)
input2 = torch.tensor([-1.0, 1.0, -0.5], requires_grad=True)
target = torch.tensor([1, -1, 1], dtype=torch.int64)

# Call the API
criterion = torch.nn.HingeEmbeddingLoss(reduction='mean')
loss = criterion(input1, input2, target)

print(loss)