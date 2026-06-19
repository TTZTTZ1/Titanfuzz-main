import torch

class MyDataset(torch.utils.data.Dataset):

    def __init__(self):
        self.data = torch.randn(5, 10)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
dataset = MyDataset()