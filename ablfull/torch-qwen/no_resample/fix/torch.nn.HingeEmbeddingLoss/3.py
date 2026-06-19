import torch
input1 = torch.tensor([1.0, (- 1.0)], requires_grad=True)
input2 = torch.tensor([(- 1.0), 1.0], requires_grad=True)
target = torch.tensor([1.0, (- 1.0)])
loss_fn = torch.nn.HingeEmbeddingLoss(reduction='mean')