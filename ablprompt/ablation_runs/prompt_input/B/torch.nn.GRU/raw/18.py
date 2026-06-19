import torch
from torch.nn import GRU
from torch.utils.data import DataLoader, TensorDataset

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
sequence_length = 5
num_batches = 4

# Create random data
input_data = torch.randn(sequence_length, batch_size, input_size)
target_data = torch.randint(0, hidden_size, (batch_size,))

# Create dataset and dataloader
dataset = TensorDataset(input_data, target_data)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Initialize GRU model
gru_model = GRU(input_size, hidden_size, num_layers, batch_first=True)

# Forward pass
for batch_input, batch_target in dataloader:
    output, _ = gru_model(batch_input)
    print(output.shape)  # Should be (batch_size, sequence_length, hidden_size)