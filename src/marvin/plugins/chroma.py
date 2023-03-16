from marvin.infra.chroma import Chroma
from marvin.plugins import Plugin
from marvin.utilities.strings import slice_tokens


async def query_chroma(query: str, n: int = 4):
    chroma = Chroma()
    results = await chroma.query(
        query_texts=[query],
        n_results=n,
        include=["documents", "metadatas"],
    )
    return "\n\n".join(
        f"({link}): {doc}"
        for link, doc in zip(results["ids"], results["documents"])
    )
class SearchChromaEmbeddings(Plugin):
    description: str = (
        "Search Chroma for documents similar to a query - "
        "Use this plugin when asked about prefect."
    )

    async def run(self, query: str) -> str:
        result = await query_chroma(query)
        print(result + "\n\n" + query)
        return result