hay que ajustar bs al tamaño de bytes devuelto por el script generate_index.py


# LÍNEA 0
out=$(dd if=rockyou_1k.txt.idx bs=8 skip=0 count=1 2>/dev/null)
off=$(cut -d' ' -f1 <<< "$out")
len=$(cut -d' ' -f2 <<< "$out")
dd if=rockyou_1k.txt bs=1 skip=$off count=$len 2>/dev/null

# LÍNEA 1
out=$(dd if=rockyou_1k.txt.idx bs=6 skip=1 count=1 2>/dev/null)
off=$(cut -d' ' -f1 <<< "$out")
len=$(cut -d' ' -f2 <<< "$out")
dd if=rockyou_1k.txt bs=1 skip=$off count=$len 2>/dev/null

# LÍNEA 2
out=$(dd if=rockyou_1k.txt.idx bs=6 skip=2 count=1 2>/dev/null)
off=$(cut -d' ' -f1 <<< "$out")
len=$(cut -d' ' -f2 <<< "$out")
dd if=rockyou_1k.txt bs=1 skip=$off count=$len 2>/dev/null

# LÍNEA 3
out=$(dd if=rockyou_1k.txt.idx bs=6 skip=3 count=1 2>/dev/null)
off=$(cut -d' ' -f1 <<< "$out")
len=$(cut -d' ' -f2 <<< "$out")
dd if=rockyou_1k.txt bs=1 skip=$off count=$len 2>/dev/null

# LÍNEA 4
out=$(dd if=rockyou_1k.txt.idx bs=6 skip=4 count=1 2>/dev/null)
off=$(cut -d' ' -f1 <<< "$out")
len=$(cut -d' ' -f2 <<< "$out")
dd if=rockyou_1k.txt bs=1 skip=$off count=$len 2>/dev/null