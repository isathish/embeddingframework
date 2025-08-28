import asyncio
import argparse
from embeddingframework.processors.file_processor import FileProcessor
from embeddingframework.adapters.openai_embedding_adapter import OpenAIEmbeddingAdapter
from embeddingframework.adapters.vector_dbs import ChromaDBAdapter, PineconeAdapter, WeaviateAdapter, MilvusAdapter
from embeddingframework.adapters.storage.s3_storage_adapter import S3StorageAdapter


async def main():
    parser = argparse.ArgumentParser(description="Async Embedding Framework")
    parser.add_argument("--files", nargs="+", required=True, help="List of file paths to process")
    parser.add_argument("--vector-db", choices=["chroma", "pinecone", "weaviate", "milvus"], default="chroma")
    parser.add_argument("--embedding-model", choices=["openai"], default="openai")
    parser.add_argument("--chunk-size", type=int, default=1024*1024, help="Binary chunk size in bytes")
    parser.add_argument("--text-chunk-size", type=int, default=500, help="Text chunk size in characters")
    parser.add_argument("--merge-target-size", type=int, default=None, help="Merge smaller chunks into this size")
    parser.add_argument("--parallel", action="store_true", help="Enable parallel chunk processing")
    parser.add_argument("--file-parallel", action="store_true", help="Enable parallel file processing")
    parser.add_argument("--bandwidth-limit", type=int, default=None, help="Max bytes/sec for streaming")
    parser.add_argument("--cloud-storage", choices=["s3", "gcs", "azure"], help="Optional cloud storage backend")
    parser.add_argument("--bucket-name", type=str, help="Bucket/container name for cloud storage")
    parser.add_argument("--cloud-credentials", type=str, help="Path or connection string for cloud storage credentials")
    args = parser.parse_args()

    # Select embedding adapter
    if args.embedding_model == "openai":
        embedding_adapter = OpenAIEmbeddingAdapter()

    # Select vector DB adapter
    if args.vector_db == "chroma":
        vector_db = ChromaDBAdapter()
        vector_db.connect()
        vector_db.create_collection("default")
    elif args.vector_db == "pinecone":
        vector_db = PineconeAdapter(api_key="YOUR_PINECONE_KEY", environment="us-east1-gcp", index_name="default-index")
        vector_db.connect()
    elif args.vector_db == "weaviate":
        vector_db = WeaviateAdapter(url="http://localhost:8080")
        vector_db.connect()
        vector_db.create_collection("default")
    elif args.vector_db == "milvus":
        vector_db = MilvusAdapter()
        vector_db.connect()
        vector_db.create_collection(vector_dimension=1536)

    # Select cloud storage adapter if specified
    storage_adapter = None
    if args.cloud_storage == "s3":
        from embeddingframework.adapters.storage.s3_storage_adapter import S3StorageAdapter
        storage_adapter = S3StorageAdapter(bucket_name=args.bucket_name)
    elif args.cloud_storage == "gcs":
        from embeddingframework.adapters.storage.gcs_storage_adapter import GCSStorageAdapter
        storage_adapter = GCSStorageAdapter(bucket_name=args.bucket_name, credentials_path=args.cloud_credentials)
    elif args.cloud_storage == "azure":
        from embeddingframework.adapters.storage.azure_blob_storage_adapter import AzureBlobStorageAdapter
        storage_adapter = AzureBlobStorageAdapter(container_name=args.bucket_name, connection_string=args.cloud_credentials)

    processor = FileProcessor(adapter=embedding_adapter, vector_db=vector_db)
    await processor.process_files(
        file_paths=args.files,
        chunk_size=args.chunk_size,
        text_chunk_size=args.text_chunk_size,
        merge_target_size=args.merge_target_size,
        parallel=args.parallel,
        file_level_parallel=args.file_parallel,
        bandwidth_limit=args.bandwidth_limit
    )


if __name__ == "__main__":
    asyncio.run(main())
