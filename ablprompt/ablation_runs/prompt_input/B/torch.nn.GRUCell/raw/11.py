import torch

# Define the input size and hidden size
input_size = 10
hidden_size = 20

# Create an instance of GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden states
input_data = torch.randn(5, 3, input_size)  # Batch size of 3, sequence length of 5
hidden_state = torch.zeros(3, hidden_size)   # Initial hidden state

# Process the input data through the GRUCell
for t in range(input_data.size(1)):
    hidden_state = gru_cell(input_data[:, t, :], hidden_state)

print(hidden_state)