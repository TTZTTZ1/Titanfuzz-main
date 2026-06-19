import torch
import torch.nn as nn

model = nn.Linear(10, 5)
params_to_prune = (
    (model, 'weight'),
)

prune.random_unstructured(params_to_prune, name='weight', amount=0.3)