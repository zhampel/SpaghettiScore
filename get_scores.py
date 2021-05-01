
try:
    import sys
    import argparse
    from sghettis.func_counter import FunctionCounter
    from sghettis.radon_stats import RadonStats

except ImportError as e:
    print(e)
    raise ImportError


def get_scores(args=None):
    filename = args.filename
    counter = FunctionCounter(filename)
    print('Number of functions: {}'.format(counter.function_count))

    cmplx_idx = RadonStats(filename=filename)
    rstats = cmplx_idx.analyze()
    ccomplex = cmplx_idx.ccomplex()
    hcomplex = cmplx_idx.hcomplex()
    print('Analyze: {}'.format(rstats))
    print('LOC: {}'.format(rstats.loc))
    print('CC: {}'.format(ccomplex))
    print('HC: {}'.format(hcomplex))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Get Spaghetti Score')
    parser.add_argument('-f', '--filename', dest='filename', help='Filename')
    args = parser.parse_args()
    get_scores(args=args)
