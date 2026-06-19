import torch

class MyDataset(torch.utils.data.Dataset):

    def __init__(self):
        self.data = torch.tensor([1.0, 2.0, 3.0])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]
dataset = MyDataset()