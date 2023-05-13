from typing import List


def single_fill(image: List[List[int]], sr: int, sc: int, prev_color: int, color: int) -> List[List[int]]:
    if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[sr]):
        return image

    if image[sr][sc] == color or not image[sr][sc] == prev_color:
        return image

    image[sr][sc] = color

    image = single_fill(image, sr-1, sc, prev_color, color)
    image = single_fill(image, sr+1, sc, prev_color, color)
    image = single_fill(image, sr, sc-1, prev_color, color)
    image = single_fill(image, sr, sc+1, prev_color, color)

    return image


class Solution:
    def flood_fill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        return single_fill(image, sr, sc, image[sr][sc], color)


if __name__ == "__main__":
    image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    image2 = [[0, 0, 0], [0, 0, 0]]
    res1 = Solution().flood_fill(image1, 1, 1, 2)
    res2 = Solution().flood_fill(image2, 0, 0, 0)
    print(res1)
    print(res2)