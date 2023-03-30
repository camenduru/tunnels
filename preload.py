import argparse


def preload(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--cloudflared",
        action="store_true",
        help="use trycloudflare, alternative to gradio --share",
    )

    parser.add_argument(
        "--localhostrun",
        action="store_true",
        help="use localhost.run, alternative to gradio --share",
    )

    parser.add_argument(
        "--remotemoe",
        action="store_true",
        help="use remote.moe, alternative to gradio --share",
    )

    parser.add_argument(
        "--googleusercontent",
        action="store_true",
        help="use googleusercontent.com, alternative to gradio --share",
    )

    parser.add_argument(
        "--multiple",
        action="store_true",
        help="use cloudflared and remotemoe",
    )
