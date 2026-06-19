import torch
input1 = torch.randn(5)
input2 = torch.randn(5)
target = torch.randint(0, 2, (5,))
margin = 1.0
loss_fn = torch.nn.HingeEmbeddingLoss(margin=margin)