#!/usr/bin/env python3

import subprocess
import argparse

alg = ["md5sum", "sha1sum", "sha256sum", "sha512sum"]

argparser = argparse.ArgumentParser()
argparser.add_argument("-f", dest="file", type=str, help="Input file to calculate hash")
argparser.add_argument("-H", dest="hash", type=str, help="Hash string to compare with")
argparser.add_argument("-e", dest="encode", type=str, default=None, help="Encoding to use for hash calculation")
argparser.add_argument("-a", dest="algorithm", type=int, default=2, help="0=MD5, 1=SHA1, 2=SHA256 (def), 3=SHA512")
args = argparser.parse_args()

if args.encode is None:
    result = subprocess.run([alg[args.algorithm], args.file], stdout=subprocess.PIPE)
else:
    result = subprocess.run([args.encode, args.file], stdout=subprocess.PIPE)
calculated_hash = (str(result.stdout, 'utf-8').split(' ', 1)[0]).upper()
provided_hash = args.hash.upper()   

if calculated_hash == provided_hash:
    print(f"Hash ok!\n{calculated_hash}")
else:
    print(f"\n\nWARNING!!!\tHash mismatch!!!")
    print(f"provided\t{provided_hash}\ncalculated\t{calculated_hash}")
