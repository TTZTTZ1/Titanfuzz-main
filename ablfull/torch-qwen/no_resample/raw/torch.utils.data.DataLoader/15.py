import torch

# Create a dummy dataset
class DummyDataset(torch.utils.data.Dataset):
    def __len__(self):
        return 10

    def __getitem__(self, idx):
        return torch.tensor([idx])

dataset = DummyDataset()

# Call DataLoader with valid parameters
dataloader = torch.utils.data.DataLoader(
    dataset=dataset,
    batch_size=2,
    shuffle=False,
    num_workers=0,
    prefetch_factor=2,
    persistent_workers=False
)