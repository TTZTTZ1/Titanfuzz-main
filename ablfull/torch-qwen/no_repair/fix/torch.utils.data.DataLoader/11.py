
import torch
from torch.utils.data import DataLoader, TensorDataset
data = torch.randn(10, 3)
dataset = TensorDataset(data)
dataloader = DataLoader(dataset, batch_size=2, shuffle=False)
for batch in dataloader:
    print(batch)
