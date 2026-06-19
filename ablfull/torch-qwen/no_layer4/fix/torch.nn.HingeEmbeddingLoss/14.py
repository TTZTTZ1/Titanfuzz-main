import torch
input1 = torch.tensor([1.0, (- 1.0), 0.5], dtype=torch.float)
input2 = torch.tensor([(- 1.0), 1.0, (- 0.5)], dtype=torch.float)
target = torch.tensor([1, (- 1), 1], dtype=torch.long)
loss_fn = torch.nn.HingeEmbeddingLoss(reduction='mean')