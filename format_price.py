import argparse


def format_price(price):
    try:
        return '{:,.0f}'.format(float(price)).replace(',', ' ')
    except (ValueError, SyntaxError, TypeError):
        return None


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input',
        help='Input price',
        required=True,
        type=float
    )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    print(format_price(args.input))
