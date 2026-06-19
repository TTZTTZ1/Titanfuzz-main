import torch

# Define the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden/cell states
input_data = torch.randn(5, 10)  # Batch size of 5, sequence length of 5, input size of 10
hidden_state = torch.zeros(5, 20)  # Batch size of 5, hidden size of 20
cell_state = torch.zeros(5, 20)   # Batch size of 5, hidden size of 20

# Process the input through the LSTMCell
for t in range(input_data.size(0)):
    hidden_state, cell_state = lstm_cell(input_data[t], (hidden_state, cell_state))

print(hidden_state)
print(cell_state)