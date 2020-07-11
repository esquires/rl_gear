from setuptools import setup

setup(
    name='rl_gear',
    version='0.0.1',
    author='Eric Squires',
    long_description='',
    description='',
    zip_safe=False,
    packages=['rl_gear'],
    install_requires=[
        "git-python",
        "crc32c",
        "ray[debug]",
        "ray[tune]",
        "ray[rllib]",
        "dm-tree",
        "tabulate",
    ],
    entry_points={
        'console_scripts':
            ['tensorboard-mean-plot=rl_gear.scripts:tensorboard_mean_plot'],
    }
)
