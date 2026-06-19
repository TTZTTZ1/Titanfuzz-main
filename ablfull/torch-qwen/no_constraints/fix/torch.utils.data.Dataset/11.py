import torch

class SimpleDataset(torch.utils.data.Dataset):

    def __init__(self):
        self.data = torch.tensor([[1, 2], [3, 4], [5, 6]])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
dataset = SimpleDataset()