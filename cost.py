from typing import List

from hypothesis import hypothesis


def cost(x: List[float], y: List[float], z: List[float]) -> float:
    loss = 0.0
    nn = min(x.__len__(), y.__len__(), z.__len__())
    for i in range(nn):
        loss += pow(hypothesis(x[i], y[i]) - z[i], 2)
    return loss / (2 * nn)
