from setuptools import setup

setup(
    name='django_fstore',
    version='0.0.4',
    author='bigtiger',
    author_email='chinafengheping@gmail.com',
    url='http://www.hshl.ltd',
    description=u'minio for django store. ',
    packages=['django_store'],
    install_requires=[
        'minio>=5.0.5',
        'deprecation>=2.0.1'
    ]
)
