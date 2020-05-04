import os
import sys
from zipfile import ZipFile

def gen_passwd_elems(args):
    total_elems = []
    if args.a: #use lower letter
        lower_word  = [chr(ord('a') + i) for i in range(26)]
        total_elems.extend(lower_word)

    if args.A: #use upper letter
        upper_word = [chr(ord('A') + i) for i in range(26)]
        total_elems.extend(upper_word)

    if args.spec: #use user spec letter
        total_elems.extend(list(set(args.spec)))

    if args.n: #user numeric
        digits = [i for i in range(10)]
        total_elems.extend(digits)

    return total_elems

def gen_passwd_iter(elements, pwnums=6, curnum=1):
    for i in elements:
        if pwnums == curnum:
            yield str(i)
        else:
            for j in gen_passwd_iter(elements, pwnums, curnum+1):
                yield str(i) + str(j)

if __name__ == "__main__":
    from args import setup_args

    args = setup_args()
    filename = args.filepath
    passwd_len = int(args.N)
    passwd_words = gen_passwd_elems(args)

    zfile = ZipFile(os.path.abspath(filename))
    for l in range(1, passwd_len+1):
        for pwd in gen_passwd_iter(passwd_words, l, 1):
            try:
                zfile.extractall(pwd=pwd.encode('utf-8'))
                print('Try password:{0} successed.'.format(pwd))
                sys.exit(0)
            except Exception as e:
                print('Try password:{1} failed! Error:{0}'.format(e, pwd))




