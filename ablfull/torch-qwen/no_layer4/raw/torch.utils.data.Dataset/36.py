import torch

# Example input data that satisfies the constraints of torch.utils.data.Dataset
class MyDataset(torch.utils.data.Dataset):
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# Create an instance of the custom dataset
dataset = MyDataset()

# Call the API with the prepared input data
print(dataset[0])  # Output should be 1