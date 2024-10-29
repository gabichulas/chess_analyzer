import pandas as pd

cols = ['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 
 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 
 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 
 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 
 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 
 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 
 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 
 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
 'Color', 'Evaluation']

def parse_deck(fen): 
    rows = fen.split(' ')[0].split('/')
    
    board = []
    for row in rows:
        expanded_row = ''
        for char in row:
            if char.isdigit():
                expanded_row += ' ' * int(char)
            else:
                expanded_row += char
        board.extend(list(expanded_row))
    
    # Asegurarse de que board tenga exactamente 64 elementos
    if len(board) != 64:
        raise ValueError("El tablero generado no tiene 64 elementos")

    # Agregar 'Color' y 'Evaluation'
    board.append(fen.split(' ')[1])  # Color
    
    return board

def parse_df(df):
    global cols
    decks = []
    for _, row in df.iterrows():
        deck = parse_deck(row['FEN']) + row['Evaluation']
        decks.append(deck)
    new_df = pd.DataFrame(decks, columns=cols)
    return new_df


# Ejemplo
fen = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1" # Peon blanco a e4
fen = parse_deck(fen)

#print(fen) # ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'P', 'P', 'P', 'P', ' ', 'P', 'P', 'P', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']


df = pd.read_csv(r"data\chessData.csv")
new_df = parse_df(df)
print(new_df.head())






