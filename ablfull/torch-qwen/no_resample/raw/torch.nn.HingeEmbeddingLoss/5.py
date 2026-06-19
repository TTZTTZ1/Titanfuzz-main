import torch

# Prepare valid input data
input1 = torch.tensor([1.0, -1.0], requires_grad=True)
input2 = torch.tensor([-1.0, 1.0], requires_grad=True)
target = torch.tensor([1, -1])

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')
loss = loss_fn(input1, input2, target)

print(loss)