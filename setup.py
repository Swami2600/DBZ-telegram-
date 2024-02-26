from setuptools import setup, find_packages

setup(
    name='dragon-ball-z-telegram-bot',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'python-telegram-bot==13.7'
        # Add any other dependencies your project requires
    ],
    entry_points={
        'console_scripts': [
            'dragon-ball-z-telegram-bot=dragon_ball_z_telegram_bot.bot:main'
        ]
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A Telegram bot based on the Dragon Ball Z theme.',
    url='https://github.com/Swami260//DBZ-telegram-,
)
