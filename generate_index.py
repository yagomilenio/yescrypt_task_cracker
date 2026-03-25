import struct
import os

"""
">"  →  big-endian (el byte más significativo va primero)
"Q"  →  unsigned long long = entero de 8 bytes (offset, máx 18 petabytes)
"I"  →  unsigned int       = entero de 4 bytes (length, máx 4 GB por registro)

de este modo me deja 12 bytes es decir 12 caracteres
"""

def max_offset_from_file(filepath: str) -> int: #retorna el valor en bytes
    size = os.path.getsize(filepath)



def max_chars_between_delimiter(filepath: str, delimiter: bytes = b'\n') -> int:
    max_len = 0

    with open(filepath, "rb") as f:
        for line in f:
            length = len(line.rstrip(delimiter))
            if length > max_len:
                max_len = length

    return max_len


def get_struct_format(max_len: int, max_offset: int) -> struct.Struct:
    # elegir tipo para length
    if max_len <= 0xFF:
        len_fmt = "B"      # 1 byte,  máx 255
    elif max_len <= 0xFFFF:
        len_fmt = "H"      # 2 bytes, máx 65,535
    else:
        len_fmt = "I"      # 4 bytes, máx 4GB

    # elegir tipo para offset
    if max_offset <= 0xFFFF:
        off_fmt = "H"      # 2 bytes
    elif max_offset <= 0xFFFFFFFF:
        off_fmt = "I"      # 4 bytes
    else:
        off_fmt = "Q"      # 8 bytes

    fmt = f">{off_fmt}{len_fmt}"
    return struct.Struct(fmt)



def generate_index(data_file: str, index_file: str):
    import os
    file_size = os.path.getsize(data_file)
    max_len = max_chars_between_delimiter(data_file)
    INDEX_ENTRY = get_struct_format(max_len, file_size)
    print(f"max_len={max_len}, file_size={file_size}, formato={INDEX_ENTRY.format}, bytes por entrada={INDEX_ENTRY.size}")
    with open(data_file, "rb") as datos, open(index_file, "wb") as idx:
        offset = 0
        for line in datos:
            idx.write(INDEX_ENTRY.pack(offset, len(line)))
            offset += len(line)

    print(f"offset_bytes={INDEX_ENTRY.size - 1}, length_bytes=1, entry_size={INDEX_ENTRY.size}")




if __name__ == "__main__":

    max_offset = max_offset_from_file("rockyou.txt")

    generate_index("rockyou_1k.txt", "rockyou_1k.idx")