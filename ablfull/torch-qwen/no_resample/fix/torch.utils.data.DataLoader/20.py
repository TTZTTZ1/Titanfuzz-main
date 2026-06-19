import torch
dataset = torch.utils.data.TensorDataset(torch.randn(10, 3))
batch_size = 2
shuffle = True
sampler = None
batch_sampler = None
num_workers = 1
collate_fn = None
pin_memory = False
drop_last = False
timeout = 0
worker_init_fn = None
multiprocessing_context = 'spawn'
generator = None
prefetch_factor = 2
persistent_workers = False
pin_memory_device = ''
in_order = True
dataloader = torch.utils.data.DataLoader(dataset=dataset, batch_size=batch_size, shuffle=shuffle, sampler=sampler, batch_sampler=batch_sampler, num_workers=num_workers, collate_fn=collate_fn, pin_memory=pin_memory, drop_last=drop_last, timeout=timeout, worker_init_fn=worker_init_fn, multiprocessing_context=multiprocessing_context, generator=generator, prefetch_factor=prefetch_factor, persistent_workers=persistent_workers, pin_memory_device=pin_memory_device, in_order=in_order)