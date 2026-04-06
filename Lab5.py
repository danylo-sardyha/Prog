def flood_fill(matrix, start_row, start_col, new_color):
    """
    Flood fill
    """
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    

    if rows == 0 or cols == 0 or start_row < 0 or start_row >= rows or start_col < 0 or start_col >= cols:
        return matrix
    
    target_color = matrix[start_row][start_col]
    
    if target_color == new_color:
        return matrix

    def dfs(r, c):

        if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != target_color:
            return
        
 
        matrix[r][c] = new_color
        

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    dfs(start_row, start_col)
    return matrix


def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]
            
        if len(lines) < 4:
            print("Помилка: Недостатньо даних у файлі input.txt")
            return
        
        height, width = map(int, lines[0].split(','))
        start_row, start_col = map(int, lines[1].split(','))
        new_color = lines[2].strip(" '\"‘’")
        matrix = []

        for line in lines[3:]:
            clean_elements = [char.strip(" '\"‘’[]") for char in line.split(',')]
            row = [char for char in clean_elements if char]
            if row:
                matrix.append(row)

        result_matrix = flood_fill(matrix, start_row, start_col, new_color)

        with open('output.txt', 'w', encoding='utf-8') as f:
            for i, row in enumerate(result_matrix):
                line_str = str(row)
                if i < len(result_matrix) - 1:
                    line_str += ','
                f.write(line_str + '\n')
                
        print("Успіх! Алгоритм виконав заливку. Перевірте файл output.txt.")

    except FileNotFoundError:
        print("Помилка: Файл input.txt не знайдено. Створіть його у тій самій папці, де знаходиться скрипт.")
    except Exception as e:
        print(f"Сталася неочікувана помилка під час обробки: {e}")

if __name__ == '__main__':
    main()