import torch
from torch.nn import GRU
from torch.utils.data import DataLoader, TensorDataset

# Define the model
input_size = 10
hidden_size = 20
num_layers = 2
gru = GRU(input_size, hidden_size, num_layers, batch_first=True)

# Create dummy data
seq_len = 5
batch_size = 3
input_data = torch.randn(seq_len, batch_size, input_size)
target_data = torch.randint(0, hidden_size, (seq_len, batch_size))

# Prepare dataset and dataloader
dataset = TensorDataset(input_data, target_data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Forward pass
for input_seq, target_seq in dataloader:
    output, _ = gru(input_seq)
    loss = torch.mean((output - target_seq) ** 2)
    print(f"Loss: {loss.item()}")