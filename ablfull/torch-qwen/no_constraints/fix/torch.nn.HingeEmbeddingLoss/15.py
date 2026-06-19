import torch
input1 = torch.randn(5)
input2 = torch.randn(5)
target = torch.randint(0, 2, (5,), dtype=torch.long)
loss_fn = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')