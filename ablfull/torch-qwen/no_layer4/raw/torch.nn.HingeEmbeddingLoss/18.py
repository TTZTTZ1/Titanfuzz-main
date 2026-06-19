import torch

# Prepare input data
input1 = torch.tensor([1.0, -1.0, 0.5])
input2 = torch.tensor([-1.0, 1.0, -0.5])

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')
loss = loss_fn(input1, input2)

print(loss)