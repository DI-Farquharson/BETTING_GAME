import pickle

path = "C:\\Users\\DI\\OneDrive\\Documents\\GitHub\\BETTING_GAME\\BETTING_GAME\\file.bin"
with open(path, 'rb') as file:
    print(pickle.load(file))