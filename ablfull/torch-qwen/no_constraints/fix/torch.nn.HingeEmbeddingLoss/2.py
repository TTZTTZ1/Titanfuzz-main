import torch
input1 = torch.tensor([1.0, (- 1.0), 0.5])
input2 = torch.tensor([(- 1.0), 1.0, (- 0.5)])
target = torch.tensor([1, (- 1), 1])
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')