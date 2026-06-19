import torch

# Create a dummy dataset
class DummyDataset(torch.utils.data.Dataset):
    def __len__(self):
        return 10

    def __getitem__(self, idx):
        return torch.tensor([idx])

dataset = DummyDataset()

# Initialize DataLoader with valid parameters
dataloader = torch.utils.data.DataLoader(
    dataset=dataset,
    batch_size=2,
    shuffle=False,
    sampler=None,
    batch_sampler=None,
    num_workers=0,
    collate_fn=None,
    pin_memory=False,
    drop_last=False,
    timeout=0,
    worker_init_fn=None,
    multiprocessing_context=None,
    generator=None,
    prefetch_factor=2,
    persistent_workers=False,
    pin_memory_device='',
    in_order=True
)