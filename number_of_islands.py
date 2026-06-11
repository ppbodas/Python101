
def num_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    print(f"Rows {rows}")
    print(f"Cols {cols}")
    visited = [cols*[-1] for i in range(rows)]
    print(grid)
    print (visited)

    count = 0
    for i in range(rows):
        for j in range(cols):
            # print(grid[i][j])
            # print(visited[i][j])
            if grid[i][j] == "1":
                if visited[i][j] == -1:
                    # print("Reached here")
                    count = count + 1
                    dfs(grid, i, j, visited)

    print(f"Number of islands {count}")
    return count

pairs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def dfs(grid, i, j, visited):
    rows = len(grid)
    cols = len(grid[0])

    for pair in pairs:
        l_row = i + pair[0]
        l_col = j + pair[1]

        if not 0 <= l_row < rows: continue
        if not 0 <= l_col < cols: continue

        if grid[l_row][l_col] == "1":
            if visited[l_row][l_col] == -1:
                visited[l_row][l_col] = 1
                dfs(grid, l_row, l_col, visited)

if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_islands(grid1) == 1

    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(grid2) == 3

    grid3 = [["1"]]
    assert num_islands(grid3) == 1

    grid4 = [["0"]]
    assert num_islands(grid4) == 0

    print("All tests passed")
