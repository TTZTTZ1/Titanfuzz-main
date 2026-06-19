import torch

class MyDataset(torch.utils.data.Dataset):
    def __init__(self):
        pass

    def __len__(self):
        return 10

    def __getitem__(self, idx):
        return torch.tensor([idx])

dataset = MyDataset()