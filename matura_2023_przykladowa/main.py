def number_of_empty_columns(position):
    empty = 0
    for i in range(8):
        is_empty = True
        for j in range(8):
            if position[j][i] != '.':
                is_empty = False
        if is_empty:
            empty += 1
    return empty


def pieces(position):
    white, black = ([],[])
    for row in position:
        for tile in row:
            if tile == '.':
                pass
            elif tile == tile.upper():
                white.append(tile)
            else:
                black.append(tile.upper())
    white.sort()
    black.sort()
    return white, black


def piece_coordinates(position, piece):
    for i in range(8):
        for j in range(8):
            if position[i][j] == piece:
                coords = (i, j)
    return coords


def is_rook_checking(position, coords, king_color):
    if king_color == 'white':
        rook = 'w'
    else:
        rook = 'W'
    x, y = coords
    checking = False
    check_temp = False

    for i in range(0, x):
        tile = position[i][y]
        if tile == rook:
            check_temp = True
        elif tile != '.':
            check_temp = False
    if check_temp:
        checking = True

    for i in range(7, x, -1):
        tile = position[i][y]
        if tile == rook:
            check_temp = True
        elif tile != '.':
            check_temp = False
    if check_temp:
        checking = True

    for i in range(0, y):
        tile = position[x][i]
        if tile == rook:
            check_temp = True
        elif tile != '.':
            check_temp = False
    if check_temp:
        checking = True

    for i in range(7, y, -1):
        tile = position[x][i]
        if tile == rook:
            check_temp = True
        elif tile != '.':
            check_temp = False
    if check_temp:
        checking = True

    return checking


if __name__ == '__main__':
    with open("szachy.txt", 'r') as file:
        game = [[[*line] for line in position.split('\n')] for position in file.read().split('\n\n')]
    print(game)

    # Podaj, na ilu planszach znajude się przynajmniej jenda pusta kolumna, czyli taka, na polach której nie stoi
    # żadna bierka. Podaj także największą liczbę pustych kolumn na jednej z tych plansz.

    positions_with_empty_columns = 0
    max_empty_columns = 0
    for position in game:
        empty_columns = number_of_empty_columns(position)
        if empty_columns > 0:
            positions_with_empty_columns += 1
        if empty_columns > max_empty_columns:
            max_empty_columns = empty_columns

    print()
    print('################################################################################')
    print('Podaj, na ilu planszach znajude się przynajmniej jenda pusta kolumna, czyli taka, na polach której nie stoi')
    print('żadna bierka. Podaj także największą liczbę pustych kolumn na jednej z tych plansz.')
    print(f'Istnieje {positions_with_empty_columns} takich plansz.')
    print(f'Największa liczba pustych kolumna na jednej planszy to {max_empty_columns}')
    print('################################################################################')
    print()

    # Rozstrzygnij, ile razy w trakcie gry (inaczej: na ilu planszach zapisanych w pliku szachy.txt) nastąpiła
    # sytuacja, w której jest równowaga – jest tyle samo i takich samych czarnych bierek, ile białych. Podaj liczbę
    # takich plansz, a także najmniejszą liczbę bierek (łącznie białych i czarnych) na planszy w stanie równowagi.

    equal_positions = 0
    min_equal_pieces = 32
    for position in game:
        white_pieces, black_pieces = pieces(position)
        if white_pieces == black_pieces:
            equal_positions += 1
            if len(white_pieces)*2 < min_equal_pieces:
                min_equal_pieces = len(white_pieces)*2

    print()
    print('################################################################################')
    print('Rozstrzygnij, ile razy w trakcie gry (inaczej: na ilu planszach zapisanych w pliku szachy.txt) nastąpiła')
    print('sytuacja, w której jest równowaga – jest tyle samo i takich samych czarnych bierek, ile białych. Podaj liczbę')
    print('takich plansz, a także najmniejszą liczbę bierek (łącznie białych i czarnych) na planszy w stanie równowagi.')
    print(f'Sytuacja równowagi nastąpiła {equal_positions} razy.')
    print(f'Najmniejsza liczba bierek w stanie równowagi wyniosła {min_equal_pieces} bierki.')
    print('################################################################################')
    print()

    # Wieża szachuje króla przeciwnego gracza, jeśli znajduje się w tym samym wierszu lub w tej samej kolumnie co
    # król i pomiędzy nimi nie ma żadnej innej bierki. Oblicz i podaj, na ilu planszach biała wieża szachuje czarnego
    # króla oraz na ilu planszach czarna wieża szachuje białego króla.

    white_rook_checks, black_rook_checks = (0, 0)
    for position in game:
        white_king_pos = piece_coordinates(position, 'K')
        black_king_pos = piece_coordinates(position, 'k')
        if is_rook_checking(position, black_king_pos, 'black'):
            white_rook_checks += 1
        if is_rook_checking(position, white_king_pos, 'white'):
            black_rook_checks += 1

    print()
    print('################################################################################')
    print('Wieża szachuje króla przeciwnego gracza, jeśli znajduje się w tym samym wierszu lub w tej samej kolumnie co')
    print('król i pomiędzy nimi nie ma żadnej innej bierki. Oblicz i podaj, na ilu planszach biała wieża szachuje czarnego')
    print('króla oraz na ilu planszach czarna wieża szachuje białego króla.')
    print(f'Biała wieża szachuje czarnego króla {white_rook_checks} razy.')
    print(f'Czarna wieża szachuje białego króla {black_rook_checks} razy.')
    print('################################################################################')
    print()
