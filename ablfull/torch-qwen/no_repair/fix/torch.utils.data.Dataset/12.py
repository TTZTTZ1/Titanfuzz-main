
import torch
from torch.utils.data import Dataset

class CustomDataset(Dataset):

    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = {'data': self.data[idx], 'target': self.targets[idx]}
        return sample
dummy_data = torch.randn(5, 3)
dummy_targets = torch.randint(0, 2, (5,))
dataset = CustomDataset(dummy_data, dummy_targets)
