import numpy.random as npr
from scanpy.sc import AnnData
from time import time

def run_baseline(
    adata: AnnData,
    n_cluster: int,
    timings: dict[str, None | float],
    clustering_info: dict[str, dict[str, None | float | int]],
    seed: int = 42,
) -> AnnData:
    # generate random cluster assignments ####
    start_time = time()
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

    return adata
