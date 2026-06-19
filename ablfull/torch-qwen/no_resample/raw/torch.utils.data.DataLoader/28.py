import torch
from torch.utils.data import DataLoader, TensorDataset

# Prepare valid input data
dataset = TensorDataset(torch.randn(10, 3), torch.randint(0, 2, (10,)))
batch_size = 2
shuffle = False
sampler = None
batch_sampler = None
num_workers = 0
collate_fn = None
pin_memory = False
drop_last = False
timeout = 0
worker_init_fn = None
multiprocessing_context = None
generator = None
prefetch_factor = 2
persistent_workers = False
pin_memory_device = ''
in_order = True

# Call the API
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle, sampler=sampler, batch_sampler=batch_sampler, num_workers=num_workers, collate_fn=collate_fn, pin_memory=pin_memory, drop_last=drop_last, timeout=timeout, worker_init_fn=worker_init_fn, multiprocessing_context=multiprocessing_context, generator=generator, prefetch_factor=prefetch_factor, persistent_workers=persistent_workers, pin_memory_device=pin_memory_device, in_order=in_order)