import torch
input1 = torch.randn(3)
input2 = torch.randn(3)
target = torch.tensor([1, (- 1), 1])
loss_fn = torch.nn.HingeEmbeddingLoss()