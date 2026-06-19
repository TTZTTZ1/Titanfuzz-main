import torch

class MyDataset(torch.utils.data.Dataset):

    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
data = [torch.randn(3, 224, 224) for _ in range(10)]
dataset = MyDataset(data)