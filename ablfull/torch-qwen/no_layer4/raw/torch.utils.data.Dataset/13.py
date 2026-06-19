import torch

class MyDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.data = torch.randn(10, 3, 256, 256)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Create an instance of the dataset
dataset = MyDataset()

# Example usage of the dataset
sample = dataset[0]
print(sample.shape)