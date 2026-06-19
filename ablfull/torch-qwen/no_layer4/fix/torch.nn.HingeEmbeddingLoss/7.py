import torch
input1 = torch.tensor([1.0, (- 1.0)])
input2 = torch.tensor([1.0, (- 1.0)])
target = torch.tensor([(- 1), 1])
loss_fn = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')