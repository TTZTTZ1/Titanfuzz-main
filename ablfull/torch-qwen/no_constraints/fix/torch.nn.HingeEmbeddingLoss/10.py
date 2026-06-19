import torch
input1 = torch.tensor([1.0, (- 1.0)], dtype=torch.float32)
input2 = torch.tensor([(- 1.0), 1.0], dtype=torch.float32)
target = torch.tensor([1.0, (- 1.0)], dtype=torch.float32)
criterion = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')