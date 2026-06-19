import torch
input1 = torch.randn(3)
input2 = torch.randn(3)
target = torch.randint(0, 2, (3,)).to(torch.float)
loss_fn = torch.nn.HingeEmbeddingLoss(reduction='mean')