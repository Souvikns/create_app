'''create-app.

Usage:
    create-app.py (-h | --help)
    create-app.py --version
    create-app.py react <params>
    create-app.py express <params>


Options:
    -h --help   Show this screen
    --version   Show Version

'''

from docopt import docopt
from func import output

ot = output()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0.0')
    if arguments['react']:
        ot.createReactApp(arguments['<params>'])
    elif arguments['express']:
        ot.createExpressApp(arguments['<params>'])
