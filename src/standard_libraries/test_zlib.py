"""Data Compression.

@see: https://docs.python.org/3/tutorial/stdlib.html#data-compression

Common data archiving and compression formats are directly supported by modules including: zlib,
gzip, bz2, lzma, zipfile and tarfile.
"""

import zlib


def test_zlib():
    """zlib."""
    string = b'witch which has which witches wrist watch'
    assert len(string) == 41

    zlib_compressed_string = zlib.compress(string)
    # NOTE: Compressed size varies across Python/zlib versions (e.g., 37 on 3.12, 41 on 3.14).
    # Verify compression produces valid output that can round-trip back to original.
    assert isinstance(zlib_compressed_string, bytes)
    assert len(zlib_compressed_string) > 0

    zlib_decompressed_string = zlib.decompress(zlib_compressed_string)
    assert zlib_decompressed_string == b'witch which has which witches wrist watch'

    assert zlib.crc32(string) == 226805979
