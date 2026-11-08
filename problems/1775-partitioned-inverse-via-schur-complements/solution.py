import numpy as np

def partitioned_inverse(M, k):
    E = M[:k, :k]
    F = M[:k, k:]
    G = M[k:, :k]
    H = M[k:, k:]
    
    H_inv_G = np.linalg.solve(H, G)
    S = E - F @ H_inv_G
    S_inv = np.linalg.inv(S)
    
    H_inv = np.linalg.inv(H)
    F_H_inv = F @ H_inv
    
    top_left = S_inv
    top_right = -S_inv @ F_H_inv
    bottom_left = -H_inv_G @ S_inv
    bottom_right = H_inv + H_inv_G @ S_inv @ F_H_inv
    
    return np.block([
        [top_left, top_right],
        [bottom_left, bottom_right]
    ])

def block_slogdet(M, k):
    E = M[:k, :k]
    F = M[:k, k:]
    G = M[k:, :k]
    H = M[k:, k:]
    
    S = E - F @ np.linalg.solve(H, G)
    
    sign_h, logdet_h = np.linalg.slogdet(H)
    sign_s, logdet_s = np.linalg.slogdet(S)
    
    sign = sign_s * sign_h
    logabsdet = logdet_s + logdet_h
    
    return sign, logabsdet

def bordered_inverse(A_inv, b, c):
    v = A_inv @ b
    s = c - b @ v
    
    if abs(s) < 1e-12:
        raise ValueError("Schur complement is too close to zero; matrix is nearly singular.")
    
    top_left = A_inv + np.outer(v, v) / s
    top_right = (-v / s)[:, np.newaxis]
    bottom_left = (-v / s)[np.newaxis, :]
    bottom_right = np.array([[1.0 / s]])
    
    return np.block([
        [top_left, top_right],
        [bottom_left, bottom_right]
    ])