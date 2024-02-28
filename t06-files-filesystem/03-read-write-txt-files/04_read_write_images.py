
# to read and write from images you need to open them in binary mode
# with open('onichophora.png', 'rb') as rf:
#     with open('onichophora_copy.png', 'wb') as wf:
#         for line in rf:
#             wf.write(line)

with open('onichophora.png', 'rb') as rf:
    with open('onichophora_chunks.png', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)