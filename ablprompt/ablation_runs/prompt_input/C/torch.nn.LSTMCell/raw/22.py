import torch

# Define the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size=10, hidden_size=20)

# Initialize input and hidden states
input_data = torch.randn(5, 10)  # Sequence of 5 timesteps, each with 10 features
hidden_state = torch.zeros(5, 20)  # Initial hidden state
cell_state = torch.zeros(5, 20)   # Initial cell state

# Process the sequence
for i in range(input_data.size(0)):
    hidden_state, cell_state = lstm_cell(input_data[i], (hidden_state, cell_state))

print("Final Hidden State:", hidden_state)
print("Final Cell State:", cell_state)