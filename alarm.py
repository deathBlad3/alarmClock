import argparse

parser = argparse.ArgumentParser()
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument('-H', '--hour', help='Hour', action='store', dest='hour', type=int, required=True)
requiredNamed.add_argument('-M','--minute', help='Minute', action='store', dest='minute', type=int, required=True)
requiredNamed.add_argument('-t', help='AM/PM', action='store', dest='ap', required=True)
args = parser.parse_args()


