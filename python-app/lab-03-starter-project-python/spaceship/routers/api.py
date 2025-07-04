from fastapi import APIRouter
import numpy as np

router = APIRouter()

@router.get("/matrices")
def multiply_matrices():
    a = np.random.rand(10, 10)
    b = np.random.rand(10, 10)
    product = np.dot(a, b)
    return {
        "matrix_a": a.tolist(),
        "matrix_b": b.tolist(),
        "product": product.tolist()
    }
