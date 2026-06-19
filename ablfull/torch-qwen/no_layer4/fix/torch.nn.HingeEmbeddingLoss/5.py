import torch
input1 = torch.tensor([1.0, (- 1.0)])
input2 = torch.tensor([(- 1.0), 1.0])
criterion = torch.nn.HingeEmbeddingLoss(reduction='mean')
output = criterion(input1, input2)
print(output)