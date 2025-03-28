input_file = "proxies.txt"  # Ganti dengan nama file input Anda
output_file = "proxies_socks5.txt"  # Nama file output

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    for line in infile:
        proxy = line.strip()
        if proxy:  # Pastikan baris tidak kosong
            outfile.write(f"socks5://{proxy}\n")

print(f"Proses selesai! Proxy yang telah diformat disimpan di {output_file}")
