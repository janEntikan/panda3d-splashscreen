import sys

from direct.showbase.ShowBase import ShowBase

from panda3d_logos.splashes import RainbowSplash

#loadPrcFileData('', 'fullscreen true')
#loadPrcFileData('', 'framebuffer-multisample 1')
#loadPrcFileData('', 'multisamples 2')


class SplashBase(ShowBase):
    def __init__(self, **kwargs):
        ShowBase.__init__(self)
        self.accept('escape', sys.exit)

        splash = RainbowSplash(**kwargs)
        self.interval = splash.setup()
        self.interval.start()
        base.task_mgr.add(self.quit_after_interval, sort=25)

    def quit_after_interval(self, task):
        if self.interval.isStopped():
            sys.exit()
        return task.cont


def main():
    from argparse import ArgumentParser
    from splashes import Pattern
    from splashes import Colors

    parser = ArgumentParser(
        description="A splash screen for Panda3D."
    )
    parser.add_argument(
        '--pattern', '-p',
        action='store', default='DOUBLE_WHEEL', type=str,
        help="Pattern: {}".format(', '.join([p.name for p in Pattern])),
    )
    parser.add_argument(
        '--colors', '-c',
        action='store', default='RAINBOW', type=str,
        help="Colors: {}".format(', '.join([p.name for p in Colors])),
    )
    parser.add_argument(
        '--pattern-freq', '-pf',
        action="store", default=1, type=float,
        help="How often the pattern is repeated",
    )
    parser.add_argument(
        '--cycle-freq', '-cf',
        action="store", default=5, type=float,
        help="Frequency of the color cycle",
    )
    opts = parser.parse_args()
    print(opts)

    app = SplashBase(
        pattern=Pattern[opts.pattern],
        colors=Colors[opts.colors],
        pattern_freq=opts.pattern_freq,
        cycle_freq=opts.cycle_freq,
    )
    app.run()


if __name__ == '__main__':
    main()
