import torch

# Define the dataset class inheriting from torch.utils.data.Dataset
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Create an instance of the custom dataset
dataset = CustomDataset()

# Access an item from the dataset
item = dataset[0]
print(item)