import torch
input1 = torch.tensor([1.0, (- 1.0)])
input2 = torch.tensor([(- 1.0), 1.0])
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')
output = criterion(input1, input2)