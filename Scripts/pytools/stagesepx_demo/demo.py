'''
轻量化的、基于图像处理与机器学习的、全自动的视频分析工具。它提供了丰富的可定制性，能够根据你的实际需求分析视频并将其拆分为一系列阶段。在此之后，你可以清晰地得知视频包含了几个阶段、以及每个阶段发生了什么。而这一切都是自动完成的。
https://testerhome.com/topics/19978
https://williamfzc.github.io/stagesepx/#/pages/0_what_is_it
'''
from stagesepx.cli import TerminalCli

cli = TerminalCli()
cli.one_step('demo.mp4')