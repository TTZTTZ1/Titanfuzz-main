import torch

# Define the dimensions
input_size = 10
hidden_size = 20

# Create a GRUCell instance
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_data = torch.randn(5, input_size)  # Batch size of 5, sequence length of 5, input size of 10
hidden_state = torch.zeros(5, hidden_size)  # Batch size of 5, hidden size of 20

# Process the sequence
for t in range(input_data.size(0)):
    hidden_state = gru_cell(input_data[t], hidden_state)

print(hidden_state)