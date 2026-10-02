# Approved archive (opaque)

This directory preserves one approved ZIP as byte-exact chunks. The archive has not been unpacked.

- Original ZIP size: 189865723 bytes
- SHA-256: `4c9f2237513112101cbdee35415eee89c97dae6c4f7c20405186729dc3ad22b6`
- Chunks: 46 (4 MiB maximum each)

## Reassemble and verify

Run with Python 3:

```sh
python3 reassemble.py
```

To choose an output path:

```sh
python3 reassemble.py --output /path/to/approved-archive.zip
```

The script validates each chunk and the complete ZIP before publishing the output file. It does not extract the archive.
