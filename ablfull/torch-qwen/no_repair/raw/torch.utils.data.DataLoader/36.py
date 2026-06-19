import torch
from torch.utils.data import DataLoader, Dataset

class DummyDataset(Dataset):
    def __len__(self):
        return 10

    def __getitem__(self, idx):
        return torch.tensor([idx])

dataset = DummyDataset()
dataloader = DataLoader(dataset, batch_size=2, shuffle=False)