import torch

class MyDataset(torch.utils.data.Dataset):
    def __init__(self, data, targets):
        self.data = data
        self.targets = targets

    def __getitem__(self, index):
        return self.data[index], self.targets[index]

    def __len__(self):
        return len(self.data)

# Prepare valid input data
data = torch.randn(10, 3, 64, 64)
targets = torch.randint(0, 10, (10,))

# Create dataset instance
dataset = MyDataset(data, targets)