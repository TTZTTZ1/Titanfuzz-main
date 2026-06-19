import torch
batch1 = torch.tensor([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
batch2 = torch.tensor([[[9, 10], [11, 12]], [[13, 14], [15, 16]]])
result = torch.bmm(batch1, batch2)
print(result)