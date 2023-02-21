"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

import os
import difflib


def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.
    dirname: string name of directory
    """
    names = []
    if '__pycache__' in dirname:
        return names

    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    """Computes the MD5 checksum of the contents of a file.
    filename: string
    """
    # Note: installing md5sha1sum is required
    
    # crio um pipe para usar a string formatada e construir 
    # o comando CertUtil -hashfile, especificando o algoritmo de hash como MD5
    # (cálculo do hash MD5 de filename - reconhecimento de duplicatas).
    
    cmd = f'CertUtil -hashfile {filename} MD5' 
    return pipe(cmd)


def check_diff(name1, name2):
    """Computes the difference between the contents of two files.
    name1, name2: string filenames
    """
    with open(name1, 'r') as file1, open(name2, 'r') as file2:
        # Read the contents of both files into two separate strings.
        content1 = file1.read()
        content2 = file2.read()

        # Use the unified_diff method from the difflib library to compare
        # the contents of the two files.
        diff = list(difflib.unified_diff(content1.splitlines(), content2.splitlines()))

        # If the length of diff is greater than 0, there are differences between
        # the two files.
        if len(diff) > 0:
            return False
        return True



def pipe(cmd):
    """Runs a command in a subprocess.
    cmd: string Unix command
    Returns (res, stat), the output of the subprocess and the exit status.
    """
    # Note: os.popen is deprecated
    # now, which means we are supposed to stop using it and start using
    # the subprocess module.  But for simple cases, I find
    # subprocess more complicated than necessary.  So I am going
    # to keep using os.popen until they take it away.

    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    """Computes checksums for all files with the given suffix.
    dirname: string name of directory to search
    suffix: string suffix to match
    Returns: map from checksum to list of files with that checksum
    """
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            res, stat = compute_checksum(name)
            checksum = res.split()[0]

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    """Checks whether any in a list of files differs from the others.
    names: list of string filenames
    """
    for name1 in names:
        for name2 in names:
            if name1 < name2:
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    """Checks for duplicate files.
    Reports any files with the same checksum and checks whether they
    are, in fact, identical.
    d: map from checksum to list of files with that checksum
    """
    for key, names in d.items():
        if len(names) > 1:
            print('The following files have the same checksum:')
            for name in names:
                print(name)

            if check_pairs(names):
                print('And they are identical.')


if __name__ == '__main__':
    d = compute_checksums(dirname='.', suffix='.py')
    print_duplicates(d)