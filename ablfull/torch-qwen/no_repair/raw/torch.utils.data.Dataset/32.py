import torch

# Define the custom dataset class
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Create some sample data
sample_data = [torch.tensor([1.0, 2.0]), torch.tensor([3.0, 4.0])]

# Initialize the dataset
dataset = CustomDataset(sample_data)