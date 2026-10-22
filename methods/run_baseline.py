import numpy.random as npr
from scanpy import AnnData
from time import time
import numpy as np
def run_baseline(
    adata: AnnData,
    n_cluster: int,
    timings: dict[str, None | float],
    clustering_info: dict[str, dict[str, None | float | int]],
    seed: int = 42,
) -> AnnData:
    # generate random cluster assignments ####
    start_time = time()
    npr.seed(seed)
    adata.obs["louvain"] = npr.randint(0, n_cluster, adata.n_obs)
    adata.obs["leiden"] = npr.randint(0, n_cluster, adata.n_obs)
    end_time = time()
    time_elapsed = end_time - start_time
    print("Time Elapsed:", time_elapsed)
    timings["cluster"] = time_elapsed
    clustering_info["resolutions"]["louvain"] = None
    clustering_info["resolutions"]["leiden"] = None
    clustering_info["num_runs"]["louvain"] = None
    clustering_info["num_runs"]["leiden"] = None
    # add placeholder for t-SNE and UMAP embeddings
    adata.obsm["X_tsne"] = np.zeros((adata.n_obs, 2))
    adata.obsm["X_umap"] = np.zeros((adata.n_obs, 2))
    # add placeholder for PCA embeddings and variance ratio
    adata.obsm["X_pca"] = np.zeros((adata.n_obs, 50))
    adata.uns["pca"] = {"variance_ratio": np.zeros(50)}
    timings["pca"] = None
    timings["t_sne"] = None
    timings["umap"] = None
    # add placeholder for highly variable genes
    adata.var["highly_variable"] = np.zeros(adata.n_vars, dtype=bool)
    
    return adata
