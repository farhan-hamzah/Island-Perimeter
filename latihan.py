from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    if r == 0 or grid[r - 1][c] == 0:
                        perimeter += 1
                    if r == rows - 1 or grid[r + 1][c] == 0:
                        perimeter += 1
                    if c == 0 or grid[r][c - 1] == 0:
                        perimeter += 1
                    if c == cols - 1 or grid[r][c + 1] == 0:
                        perimeter += 1
        return perimeter

if __name__ == "__main__":
    print("Masukkan jumlah baris:")
    rows = int(input())
    print("Masukkan jumlah kolom:")
    cols = int(input())

    print("Masukkan grid (1 untuk darat, 0 untuk air):")
    grid = []
    for i in range(rows):
        print(f"Baris ke-{i+1} (pisahkan dengan spasi, contoh: 0 1 0 1):")
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("Jumlah kolom tidak sesuai!")
            exit(1)
        grid.append(row)

    sol = Solution()
    hasil = sol.islandPerimeter(grid)
    print("Keliling pulau adalah:", hasil)
