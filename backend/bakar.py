from utils.network_utils import fetch_metadata_using_url
import asyncio
import logging
import json

logger = logging.getLogger("fastapi")

if __name__ == "__main__":
    # url = "https://zenodo.org/records/14791443"
    # url = "https://datadryad.org/stash/dataset/doi:10.5061/dryad.s1rn8pkcq"
    url = "https://doi.org/api/handles/10.5281/zenodo.6673464"
    # url = "https://huggingface.co/datasets/open-thoughts/OpenThoughts-114k"
    res = asyncio.run(fetch_metadata_using_url(url))
    print(json.dumps(res[1]))
