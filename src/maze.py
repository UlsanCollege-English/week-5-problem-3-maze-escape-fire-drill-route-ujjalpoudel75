def find_path(grid, start, end):
    """
    Return a list of (r,c) from start to end inclusive, or None if no path.
    grid contains 0 (open) and 1 (wall). Moves: up/down/left/right.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    sr, sc = start
    er, ec = end

    # Check start/end bounds and walls
    if not (0 <= sr < rows and 0 <= sc < cols) or grid[sr][sc] == 1:
        return None
    if not (0 <= er < rows and 0 <= ec < cols) or grid[er][ec] == 1:
        return None

    visited = set()
    path = []

    def backtrack(r, c):
        # Out of bounds or wall or already visited
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if grid[r][c] == 1 or (r, c) in visited:
            return False

        # Add to path and mark visited
        path.append((r, c))
        visited.add((r, c))

        # Check if reached end
        if (r, c) == (er, ec):
            return True

        # Explore 4 directions
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            if backtrack(r + dr, c + dc):
                return True

        # Backtrack
        path.pop()
        return False

    if backtrack(sr, sc):
        return path
    return None
