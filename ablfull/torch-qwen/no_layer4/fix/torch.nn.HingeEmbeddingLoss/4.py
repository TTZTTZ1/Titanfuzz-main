import torch
input1 = torch.tensor([1.0, (- 1.0)], requires_grad=True)
input2 = torch.tensor([(- 1.0), 1.0], requires_grad=True)
margin = 1.0
reduction = 'mean'
criterion = torch.nn.HingeEmbeddingLoss(margin=margin, reduction=reduction)
output = criterion(input1, input2)
print(output)