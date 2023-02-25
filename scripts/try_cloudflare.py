from pycloudflared import try_cloudflare

from modules.shared import cmd_opts

import os

if cmd_opts.cloudflared:
    print("cloudflared detected, trying to connect...")
    port = cmd_opts.port if cmd_opts.port else 7860
    tunnel_url = try_cloudflare(port=port, verbose=False)
    os.environ['webui_url'] = tunnel_url.tunnel
    os.system("sed -i '/import warnings/a from gradio import strings' /content/stable-diffusion-webui/modules/ui.py")
    os.system(f'sed -i "/from gradio import strings/a strings.en[\\"PUBLIC_SHARE_TRUE\\"] = f\\"WebUI Colab URL: {tunnel_url}\\"" /content/stable-diffusion-webui/modules/ui.py')
