import numpy as np

def k_means_clustering(
    points: list[tuple[float, ...]], 
    k: int, 
    initial_centroids: list[tuple[float, ...]], 
    max_iterations: int
) -> list[tuple[float, ...]]:
    
    final_centroids = np.array(initial_centroids, dtype=float)
    points = np.array(points, dtype=float)

    for _ in range(max_iterations):
        # 1. Mesafeyi güncel merkezlerden çıkar
        fark = points[:, np.newaxis, :] - final_centroids
        distance = np.sqrt(np.sum(fark ** 2, axis=-1))
        
        # 2. Etiketleme
        etiketler = np.argmin(distance, axis=1)
        
        # 3. Her küme için dinamik ortalama hesabı
        new_centroids = np.array([
            np.mean(points[etiketler == j], axis=0) for j in range(k)
        ])
        
        # 4. Merkezler oynamadıysa erken dur
        if np.allclose(final_centroids, new_centroids):
            break
            
        final_centroids = new_centroids

    # Beklenen çıktı formatına (list of tuples + round) dönüştürme:
    return [tuple(round(val, 4) for val in centroid) for centroid in final_centroids]