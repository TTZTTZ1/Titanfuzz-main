import torch

# Create a simple dataset
class SimpleDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.data = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Instantiate the dataset
dataset = SimpleDataset()

# Call the API
print(dataset[0])