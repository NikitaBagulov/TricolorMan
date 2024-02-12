from setuptools import setup, find_packages
setup(
    name='tricolor_person',
    version='1.0.36',
    author='Nikita bagulov',
    author_email='nikita.bagulov.arshan@gmail.com',
    description="Tricolor Test is a Python package for determining a person's color preference.",
    data_files=[('images', ['tricolorman\\images\\blue1.png',
                            'tricolorman\\images\\blue2.png',
                            'tricolorman\\images\\blue3.png',
                            'tricolorman\\images\\blue4.png',
                            'tricolorman\\images\\red1.png',
                            'tricolorman\\images\\red2.png',
                            'tricolorman\\images\\red3.png',
                            'tricolorman\\images\\red4.png',
                            'tricolorman\\images\\green1.png',
                            'tricolorman\\images\\green2.png',
                            'tricolorman\\images\\green3.png',
                            'tricolorman\\images\\green4.png',
                            'tricolorman\\images\\general.png',]), 
                    ('questions', ['tricolorman\\questions\\questions.txt'])],
    entry_points={
        'console_scripts': [
            'tricolor_person_test = tricolorman.main:main'
        ]
    },
    packages=find_packages(),
    install_requires=[
        'matplotlib',
    ]

)