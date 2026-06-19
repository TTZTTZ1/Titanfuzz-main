
import torch
input1 = torch.tensor([[1.0, (- 1.0)], [1.0, 1.0]])
input2 = torch.tensor([[1.0, 1.0], [(- 1.0), (- 1.0)]])
loss_fn = torch.nn.HingeEmbeddingLoss(reduction='mean')
loss = loss_fn(input1, input2)
print(loss)
