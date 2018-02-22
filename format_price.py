import argparse


def format_price(price):
    try:
        if price - int(price) == 0:
            return '{:,.0f}'.format(price).replace(',', ' ')
        else:
            return '{:,.2f}'.format(price).replace(',', ' ')
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
