import click
@click.command()
@click.option('--install_requires',default="",multiple=True)
@click.option('--url',default="")
@click.option('--scripts',default="",multiple=True)
@click.option('--platforms',default="",multiple=True)
@click.option('--packages',default="",multiple=True)
@click.option('--author',default="")
@click.option('--license',default="")
@click.option('--long_description',default="",multiple=True)
@click.option('--version',default="0.0.1")
@click.argument('name')
def main(**kwargs):
    import os
    os.mkdir(kwargs['name'])
    os.chdir(kwargs['name'])
    file=open("setup.py",'a+')
    file.write("from setuptools import setup\n")
    file.write("setup(\n")
    for i,j in kwargs.items():
        try:
            file.write("    "+i+"='"+j+'\',\n')
        except:
            file.write("    "+i+"="+str(list(j))+',\n')
    file.write(')')
    for i in kwargs["packages"]:
        os.mkdir(i)
        open(i+"/__init__.py","w")
main()
